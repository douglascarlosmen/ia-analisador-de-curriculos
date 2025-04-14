from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai
from werkzeug.utils import secure_filename
import fitz  # PyMuPDF para extrair texto de PDF
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configurações
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
openai.api_key = os.getenv('OPENAI_API_KEY')

# Função para extrair texto do PDF com PyMuPDF
def extract_text_from_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        text = "\n".join([page.get_text() for page in doc])
        doc.close()
        return text
    except Exception as e:
        print(f"Erro ao extrair texto do PDF: {e}")
        return ""

# Rota principal
@app.route('/api/analyze-resume', methods=['POST'])
def analyze_resume():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'Arquivo não enviado.'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    resume_text = extract_text_from_pdf(file_path)

    job_title = request.form.get('job_title', '')
    job_description = request.form.get('job_description', '')
    job_requirements = request.form.get('job_requirements', '')
    job_nice_to_have = request.form.get('job_nice_to_have', '')

    prompt = f"""
Você é um recrutador profissional. Com base na vaga abaixo, analise o seguinte currículo e responda com:
1. Compatibilidade (0 a 100)
2. Habilidades compatíveis
3. Pontos que estão faltando
4. Sugestões de melhoria

Vaga:
Título: {job_title}
Descrição: {job_description}
Requisitos: {job_requirements}
Diferenciais: {job_nice_to_have}

Currículo:
{resume_text}
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6
        )

        content = response['choices'][0]['message']['content']
        lines = content.split('\n')

        result = {
            "fit_score": lines[0].split(':')[-1].strip('% '),
            "matching_skills": lines[1].split(':', 1)[-1].strip(),
            "missing_points": lines[2].split(':', 1)[-1].strip(),
            "improvement_tips": lines[3].split(':', 1)[-1].strip()
        }
        return jsonify(result)

    except Exception as e:
        print("Erro na chamada à OpenAI:", e)
        return jsonify({'error': 'Erro ao processar a análise com a IA.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
