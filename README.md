# Ashley Toomey – Portfolio Website

A modern, responsive portfolio website built with Flask to showcase my software development projects, technical skills, and professional experience.

---

## 🌟 Features

- **Interactive Project Carousel** – Navigate through 5 coding projects with smooth horizontal scrolling  
- **Dark Mode Toggle** – Switch between professional dark/light themes  
- **Responsive Design** – Optimized for desktop, tablet, and mobile  
- **Collapsible Sections** – Expandable content areas for better UX  
- **Contact Form** – Functional form with validation and feedback  
- **Professional Stats** – Quick overview of experience and project count  
- **Social Integration** – Links to LinkedIn, GitHub, and direct contact  

---

## 🚀 Projects Showcased

- **Football Match Performance Analyzer** – GUI app for football match stats  
- **Employee Joining Date Filter** – Date range filter for employee data  
- **Python Calculator** – Desktop GUI calculator  
- **Boxing Combination Generator** – Random combo generator for training  
- **Football-Themed Registration System** – Event-driven app with pytest  

---

## 🛠️ Technology Stack

- **Backend:** Python (Flask)  
- **Frontend:** HTML5, CSS3, JavaScript  
- **Styling:** Custom CSS, responsive grid layout  
- **Icons:** Feather Icons  
- **Deployment:** Gunicorn WSGI server  

---

## 📋 Prerequisites

- Python 3.7+  
- pip (Python package manager)  

---

## 🔧 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/AshJToomey/portfolio-website.git
   cd portfolio-website

2. Create a virtual environment

python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements-dev.txt

4. Set environment variables

export SESSION_SECRET="your-secret-key-here"

5. Run the application

python app.py

6. Access the site
Open your browser at: http://localhost:5000

---

## 🚀 Production Deployment

Use Gunicorn for production:

gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app

---

## 📁 Project Structure

portfolio-website/
├── app.py
├── main.py
├── README.md
├── requirements-dev.txt
├── static/
│   ├── css/
│   │   └── style.css
│   ├── images/
│   ├── js/
│   │   └── script.js
│   └── Ashley_Toomey_CV_2025.pdf
├── templates/
│   ├── layout.html
│   └── index.html

---

## ✨ Key Features Explained

🎞️ Project Carousel
- Horizontal scroll

- Navigation arrows + dot indicators

- Fully responsive layout

🌙 Dark Mode

- Toggle between light/dark

- Smooth transitions

- Remembers user preference

✉️ Contact Form

- Form validation (client + server)

- Feedback on success or error

📱 Responsive Design

- Mobile-first

- Flexible grid

- Optimized fonts/images

---

## 🎨 Customization

➕ Add New Projects
Edit the projects list in app.py:


projects = [
    {
        "title": "New Project",
        "description": "Brief summary...",
        "image": "new_project.png",
        "github": "https://github.com/your-repo",
        "tags": ["Python", "Flask"]
    }
]

⚙️ Update Skills
Modify the skills dictionary in app.py.

🎨 Change Styles
Edit static/css/style.css for colors, layout, fonts.

---

## 🌐 Browser Support
- Chrome (latest)

- Firefox (latest)

- Safari (latest)

- Edge (latest)

---

## 🤝 Contributing
This is a personal project. Suggestions are welcome via GitHub Issues or by contacting me directly.

---

## 📄 License
Licensed under the MIT License.

---

## 📞 Contact
- Email: ashleytoomey@hotmail.com

- Phone: 07376 457737

- LinkedIn: linkedin.com/in/ashley-toomey-534601175

- GitHub: github.com/AshJToomey

Built with ❤️ by Ashley Toomey
