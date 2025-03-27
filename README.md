# BioContainer: Smart Container Suggestions for Researchers

![image](https://files.oaiusercontent.com/file-QreQnvasEYp4FKV1XP2d5M?se=2025-03-27T07%3A29%3A18Z&sp=r&sv=2024-08-04&sr=b&rscc=max-age%3D604800%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3Dd66d41d9-d858-4020-8324-ac2a80899a80.webp&sig=pj5q2HBuFixoLzghf%2Bb5l1XOJ%2BABDZRXGu6hY9HB8h4%3D)

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
1. Deploy via GitHub Actions or manually push to Netlify.
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

