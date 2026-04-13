from django.core.management.base import BaseCommand
from portfolio.models import Skill, Service, Portfolio, Experience, Education


class Command(BaseCommand):
    help = 'Seed initial data for Rizowan Kabir portfolio'

    def handle(self, *args, **kwargs):

        # Skills
        skills = [
            ('Python','language',1),('SQL','language',2),('HTML5','language',3),('CSS3','language',4),
            ('Django','framework',1),('Django REST Framework','framework',2),('Flask','framework',3),('FastAPI','framework',4),
            ('MySQL','database',1),('MongoDB','database',2),
            ('RESTful APIs','web',1),('JWT Authentication','web',2),('Session Management','web',3),('CRUD Operations','web',4),
            ('Git','tool',1),('GitHub','tool',2),('Postman','tool',3),('VS Code','tool',4),
            ('MVT Architecture','practice',1),('OOP','practice',2),('API Design','practice',3),('Bootstrap','practice',4),
        ]
        for name, cat, order in skills:
            Skill.objects.get_or_create(name=name, defaults={'category':cat,'order':order})

        # Services
        services = [
            ('Backend Development','fa-server','Building production-ready web applications using Django, Flask, and FastAPI. Implementing MVT/MVC architecture for scalable and maintainable codebases.',1),
            ('REST API Development','fa-plug','Designing and building robust RESTful APIs using Django REST Framework (DRF) and FastAPI with proper error handling, validation and serialization.',2),
            ('Database Design','fa-database','Designing efficient database schemas for MySQL and MongoDB. Query optimization, indexing, and normalization for fast and reliable data retrieval.',3),
            ('Authentication & Security','fa-shield-alt','Implementing JWT and session-based authentication systems with role-based access control (RBAC) for multi-user applications.',4),
            ('Testing & Code Quality','fa-vial','Writing unit and integration tests achieving 75%+ code coverage. Clean code principles and SOLID design patterns.',5),
            ('Version Control','fa-code-branch','Managing codebase with Git and GitHub following feature branching workflows with meaningful commit messages.',6),
        ]
        for title, icon, desc, order in services:
            Service.objects.get_or_create(title=title, defaults={'icon':icon,'description':desc,'order':order})

        # Portfolio projects
        projects = [
            ('Hospital Management System','fa-hospital','Comprehensive hospital platform with dashboards for patients, doctors, managers, and admins. Appointment booking with real-time availability, automated scheduling, and email notifications. Built secure patient record management with role-based access control.','Django, MySQL, Bootstrap',1),
            ('Job Portal Management System','fa-briefcase','Full-featured job portal connecting employers and job seekers. Resume upload with parser, application tracking, and automated email notifications for status updates. Scalable database schema supporting job postings, applications, and user profiles.','Django, MySQL, DRF, Bootstrap',2),
            ('Mini Social Media Application','fa-share-alt','Real-time social platform with posts, likes, comments, and follow/unfollow. User authentication, profile management, and news feed algorithm using MongoDB for flexible data storage.','Django, MongoDB',3),
            ('Calorie Management System','fa-apple-alt','Nutrition tracking app for monitoring daily calorie intake and fitness goals. Food database API integration for easy meal logging and detailed nutritional analysis.','Django, MySQL, Bootstrap',4),
            ('Cash Management System','fa-wallet','Financial tracking system for income, expenses, and detailed reports. Real-time analytics dashboard, budget tracking, expense categorization, and PDF export functionality.','Django, MySQL',5),
        ]
        for title, icon, desc, tech, order in projects:
            Portfolio.objects.get_or_create(title=title, defaults={'icon':icon,'description':desc,'technologies':tech,'order':order})

        # Experience
        Experience.objects.get_or_create(
            title='Backend Developer',
            defaults={
                'company':'Self-Learning & University Projects',
                'location':'IUBAT, Dhaka',
                'start_date':'Oct 2020',
                'end_date':'Mar 2025',
                'description':(
                    "Developed 5+ full-stack web applications using Django, Flask, and FastAPI with MVT & REST API architecture\n"
                    "Built production-ready CRUD APIs with DRF, implementing error handling, data validation, and serialization\n"
                    "Designed and optimized database schemas for MySQL and MongoDB with indexing & normalization\n"
                    "Implemented JWT & session-based authentication with role-based access control\n"
                    "Wrote unit & integration tests achieving 75%+ code coverage\n"
                    "Maintained clean code using Git, following feature branching workflows"
                ),
                'order':1,
            }
        )

        # Education
        Education.objects.get_or_create(
            institution='International University of Business Agriculture and Technology (IUBAT)',
            defaults={'degree':'B.Sc. in Computer Science & Engineering','location':'Dhaka, Bangladesh','start_year':'Oct 2020','end_year':'Mar 2025','cgpa':'3.20 / 4.00','icon':'fa-university','order':1}
        )
        Education.objects.get_or_create(
            institution='Dinajpur Model College',
            defaults={'degree':'Higher Secondary Certificate (HSC) – Science Group','location':'Dinajpur, Bangladesh','start_year':'2017','end_year':'2019','cgpa':'','icon':'fa-school','order':2}
        )

        self.stdout.write(self.style.SUCCESS('✅  All data seeded successfully!'))
