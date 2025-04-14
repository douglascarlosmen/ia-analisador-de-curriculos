# 🤖 Analisador de Currículos com Inteligência Artificial

Uma aplicação completa e funcional construída com **Python (Flask)** no backend e **HTML5 + Bootstrap 5** no frontend. Seu objetivo é **analisar currículos em PDF com base em descrições de vagas**, utilizando **OpenAI GPT-4** para realizar avaliações inteligentes e fornecer **feedback personalizado**, simulando um processo seletivo real.

---

## 🚀 Demonstração Rápida

📄 **Você envia um currículo em PDF**  
🧠 **A IA analisa compatibilidade com a vaga**  
📊 **Você recebe:**
- Nota de compatibilidade
- Habilidades reconhecidas
- Pontos faltantes
- Sugestões de melhoria

---

## 📌 Funcionalidades Principais

✅ Upload de currículo em PDF  
✅ Formulário completo para descrever a vaga (título, descrição, requisitos e diferenciais)  
✅ Análise de IA baseada no modelo GPT-4 (OpenAI)  
✅ Resultado exibido de forma clara e responsiva no desktop e mobile  
✅ Skeleton loading para experiência de usuário fluida  
✅ Interface moderna e intuitiva  
✅ Compatível com dispositivos móveis

---

## 🧠 Tecnologias Utilizadas

### 🔙 Backend (API Flask)
- **Flask + CORS**
- **PyMuPDF (fitz)** para extração de texto de PDFs
- **OpenAI API (GPT-4)** para análise e recomendação
- **dotenv** para variáveis de ambiente seguras
- **Werkzeug** para upload seguro de arquivos

### 🎨 Frontend
- **HTML5 + Bootstrap 5**
- **JavaScript Vanilla**
- Design **responsivo**, adaptado para mobile e desktop  
- Estilo visual moderno com efeitos de carregamento (skeleton loading)

---

## 📂 Estrutura do Projeto

```
├── app.py                  # Backend Flask: API principal
├── uploads/                # Currículos enviados são salvos aqui
├── .env                    # Armazena sua OpenAI API Key (não incluso)
├── requirements.txt        # Dependências do projeto
└── index.html              # Interface Web (frontend)
```

---

## 🛠️ Como Executar Localmente

### 1. Clone o projeto
```bash
git clone https://github.com/seuusuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2. Instale as dependências
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure sua API Key
Crie um arquivo `.env` na raiz com o seguinte conteúdo:
```env
OPENAI_API_KEY=sua-chave-da-openai
```

### 4. Inicie o servidor Flask
```bash
python app.py
```

### 5. Acesse a aplicação no navegador
```
http://localhost:5000/index.html
```

---

## 💡 Exemplo de Uso

- Preencha os campos da vaga no painel direito
- Faça upload do currículo em PDF
- Veja a análise inteligente feita pela IA no painel esquerdo
- No mobile, os resultados são exibidos em tela cheia (modal)

---

## 📥 Exemplo de Requisição para API (cURL)

```bash
curl -X POST http://localhost:5000/api/analyze-resume \
  -F "file=@seucurriculo.pdf" \
  -F "job_title=Desenvolvedor Backend" \
  -F "job_description=Responsável por manter API's REST em Python" \
  -F "job_requirements=Python, Flask, SQL" \
  -F "job_nice_to_have=Experiência com Docker"
```

---

## 🔒 Segurança

- Utiliza `secure_filename()` para evitar injeções de caminho
- API Key da OpenAI é mantida em `.env` e **não incluída no repositório**
- Pasta de uploads é criada dinamicamente e protegida por nome seguro

---

## 🧪 Próximos Passos (Ideias de Evolução)

- [ ] Suporte a múltiplos idiomas (tradução automática da vaga)
- [ ] Armazenamento do histórico de análises
- [ ] Tela de login e perfis de usuários
- [ ] Exportação do relatório de análise em PDF
- [ ] Integração com LinkedIn para importação de perfil

---

## 👨‍💼 Ideal para...

🔎 Recrutadores  
📈 Profissionais de RH  
🧑‍💻 Desenvolvedores que buscam automatizar triagens  
👨‍🎓 Estudantes em busca de autoavaliação profissional  
👔 Candidatos que desejam melhorar seus currículos com base em requisitos reais

---

## ✨ Autor

Douglas Carlos Men —  
[🔗 GitHub](https://github.com/douglascarlosmen) • [🌐 LinkedIn](https://www.linkedin.com/in/douglascarlosmen/)  
👨‍💻 +10 anos de experiência em desenvolvimento de software  
🎓 Especialista em Inteligência Artificial aplicada a negócios

---

## 📃 Licença

MIT License.  
Sinta-se livre para usar, contribuir e aprimorar este projeto. Se te ajudou, ⭐ dê uma estrela no repositório!