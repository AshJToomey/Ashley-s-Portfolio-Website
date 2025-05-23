# Ashley Toomey - Personal Portfolio Website

This is the source code for Ashley Toomey's professional portfolio website, built using **Python** and **Flask**. The website showcases Ashley's skills, experience, qualifications, projects, and contact information in a clean, user-friendly format with a dark mode toggle feature.

---

## Table of Contents

- [About](#about)  
- [Features](#features)  
- [Technologies Used](#technologies-used)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [Contact](#contact)  
- [License](#license)  

---

## About

This portfolio site presents Ashley Toomey’s background as a motivated Computer Science MEng graduate and software development enthusiast. It highlights professional experience, academic qualifications, technical skills, and personal coding projects, along with easy ways to connect via email, LinkedIn, and GitHub.

---

## Features

- Responsive design that works well on mobile and desktop  
- Dark mode toggle with persistent theme preference using `localStorage`  
- Sections including About, Experience, Qualifications, Skills, Projects, and Contact  
- Project showcase with images and links to GitHub repositories  
- Contact links with email, phone, LinkedIn, and GitHub  
- SEO-friendly meta tags and smooth scrolling navigation  

---

## Technologies Used

- **Frontend:** HTML5, CSS3 (with external stylesheet), JavaScript (for dark mode toggle)  
- **Backend:** Python with Flask web framework  
- **Templates:** Jinja2 templating engine (Flask default)  
- **Static Assets:** Images, favicon, CSS stored in `/static` directory  

---

## Installation

To run this portfolio site locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AshJToomey/ashley-portfolio.git
   cd ashley-portfolio

2. Set up a Python virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:

pip install flask

4. Run the Flask app:

flask run

5. Open your browser and visit:

http://127.0.0.1:5000/

## Usage
Navigate through the portfolio using the navigation menu

Toggle dark mode on/off with the switch in the navigation bar

Click on project links to view individual GitHub repositories

Contact Ashley using the provided email, phone, LinkedIn, or GitHub links

## Project Structure

ashley-portfolio/

│

├── app.py                  # Flask application entry point

├── templates/

│   └── index.html          # Main HTML template using Jinja2

├── static/

│   ├── css/

│   │   └── style.css       # External CSS file

│   ├── images/

│   │   └── ashley-profile.jpeg

│   ├── favicon.png

│   └── js/

│       └── (optional JS files if any)

└── README.md

## Contributing
Contributions, suggestions, and improvements are welcome!
Feel free to open an issue or submit a pull request.

## Contact
Ashley Toomey
📧 ashleytoomey@hotmail.com
📞 07376 457737
🔗 LinkedIn
💻 GitHub

## License
This project is licensed under the MIT License. See the LICENSE file for details.

© 2025 Ashley Toomey. All rights reserved.
