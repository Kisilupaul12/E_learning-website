# E-Learning Platform

## Project Overview
This E-Learning Platform is a robust web application designed to simplify online learning by providing a seamless experience for students and educators. Developed using Django, Bootstrap, and MySQL, the platform supports features such as user registration, course enrollment, and learning progress tracking. Its modular design ensures scalability and ease of integration for additional functionalities.

## Features
- **User Management**: Secure registration, login, and logout functionalities.
- **Course Management**: CRUD operations for courses, including the ability to add, edit, delete, and view courses.
- **Enrollment System**: Students can enroll in available courses.
- **Learning Materials**: Instructors can upload and manage course content.
- **Progress Tracking**: Students can monitor their course progress.
- **Payment Integration**: Support for Safaricom Daraja API for seamless payment processing.

## Tech Stack
- **Frontend**: Bootstrap, HTML, CSS, Jinja templating.
- **Backend**: Django Framework.
- **Database**: MySQL.
- **Payment API**: Safaricom Daraja API (M-Pesa).

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/elearning-platform.git
   cd elearning-platform
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate    # For Windows
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Update the `settings.py` file with your MySQL credentials.
   - Run migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

5. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application in your browser at `http://127.0.0.1:8000/`.

## Usage
- **Admins**: Manage users, courses, and learning materials via the admin panel.
- **Instructors**: Add and manage course content.
- **Students**: Browse courses, enroll, and track progress.

## Future Enhancements
- Advanced analytics for educators.
- Forums and discussion boards for students.
- Certification for completed courses.
- Mobile app integration for on-the-go learning.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any inquiries or support, please contact:
- **Name**: Paul Kisilu
- **Email**: [kisilup54@gmail.com]


---
Thank you for exploring the E-Learning Platform. Happy learning!

