# BioContainer: Smart Container Suggestions for Researchers

![A_futuristic_and_visually_appealing_cover_image_fo](https://github.com/user-attachments/assets/49f3e412-898f-46ab-ab51-e46ccd0830ef)

## 🧬 Project Overview
BioContainer simplifies containerization for **bioinformaticians and researchers** by **automatically suggesting and generating Docker/Singularity containers** based on user requirements. It removes the complexity of setting up bioinformatics environments by offering ready-to-use configurations.

## 🚀 Features
- **User Authentication** (Signup/Login)
- **Smart Container Generation** (Suggests at least two container configurations)
- **User Dashboard** (View past containers, profile settings)
- **Container Customization** (Modify and rebuild containers)
- **One-Click Deployment** (Deploy to cloud/HPC environments)

## 🛠️ Technologies Used
- **Backend:** FastAPI, PostgreSQL, SQLAlchemy
- **Frontend:** React, Axios
- **Containerization:** Docker, Singularity
- **CI/CD:** GitHub Actions, Render (Backend), Netlify (Frontend)

## 🏗️ Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/BioContainer.git
cd BioContainer
```

### **2️⃣ Backend Setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### **3️⃣ Frontend Setup**
```bash
cd ../frontend
npm install
npm start  # Runs the React app
```

## 🔗 API Endpoints
| Method | Endpoint | Description |
|--------|-------------|--------------------------------------|
| `POST` | `/register` | User signup |
| `POST` | `/login` | User login |
| `GET` | `/api/user-profile` | Get logged-in user details |
| `GET` | `/api/user-containers` | List user’s past container generations |
| `POST` | `/api/containers` | Generate new container |
| `PUT` | `/api/containers/{id}` | Modify existing container |

## 🚀 Deployment
### **Frontend (Netlify)**
1. Deploy via GitHub Actions or manually push to Netlify(Still a work in progress.
2. Set environment variables (`REACT_APP_API_URL`).

### **Backend (Render or Google Cloud Run)**
1. Deploy to **Render**:
   - Connect to GitHub, set the **Build Command**: `pip install -r requirements.txt`
   - Start with: `uvicorn main:app --host 0.0.0.0 --port 10000`
2. Set **environment variables**:
   ```bash
   DATABASE_URL=postgresql://your_user:your_password@db.supabase.co:5432/your_database
   SECRET_KEY=your-secret-key
   ```

## 📜 License
This project is licensed under the **MIT License**.

---
💡 **Contributions are welcome!** Feel free to submit issues or pull requests to improve BioContainer.

[Blog](https://medium.com/@marhwayiza325/biocontainer-smart-container-suggestions-for-researchers-f96551851658) post explaining what inspired the project and the difficulties that I faced.

## __Connect with me:__

- [Email](marhwayiza325@gmail.com)
- [LinkedIn](www.linkedin.com/in/thandeka-mavundla-01b232188)

## __Disclaimer__

The backend deployment and CI/CD deployment work, frontend deployment is still part of the continuous work that I am busy with.

## __Demo of the application (Localhost deployment of the backend)__

https://www.loom.com/share/40ab4074ae8c4f72a9bd32a2fe8c8ffd?sid=f28bfb56-bda0-4d25-943d-6bdb65b7a2d6

[Project Landing Page](https://thandeka325.github.io/biocontainer-landing/)
