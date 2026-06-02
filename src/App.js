import React, { useState, useEffect } from 'react';
import { Menu, X, Github, Linkedin, Mail, ExternalLink, Code, Award } from 'lucide-react';
import './App.css';

export default function Portfolio() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [activeSection, setActiveSection] = useState('about');
  const [codeText, setCodText] = useState(0);

  const greetings = ['👋 Hi There!', 'Welcome, I\'m', 'Ludy Hasby Aulia'];

  useEffect(() => {
    const interval = setInterval(() => {
      setCodText((prev) => (prev + 1) % 3);
    }, 2000);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    const handleScroll = () => {
      const sections = ['about', 'experience', 'skills', 'education', 'projects', 'achievement', 'contacts'];
      const current = sections.find(section => {
        const element = document.getElementById(section);
        if (element) {
          const rect = element.getBoundingClientRect();
          return rect.top <= 150 && rect.bottom >= 150;
        }
        return false;
      });
      if (current) setActiveSection(current);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
      setIsMenuOpen(false);
    }
  };

  const navItems = [
    { id: 'about', label: 'About Me', icon: '🏠' },
    { id: 'experience', label: 'Experience', icon: '💼' },
    { id: 'skills', label: 'Skills', icon: '💡' },
    { id: 'education', label: 'Education', icon: '🎓' },
    { id: 'projects', label: 'Projects', icon: '🖥️' },
    { id: 'achievement', label: 'Achievement', icon: '🏆' },
    { id: 'contacts', label: 'Contacts', icon: '📧' }
  ];

  const experiences = [
    {
      company: 'Techbros',
      role: 'Backend Developer Intern',
      period: 'November 2025 - May 2026',
      logo: '/images/techbros.jpeg',
      responsibilities: [
        'Contributed to the development of systems by building and maintaining RESTful APIs enabling reliable data processing for core business operations.',
        'Improved system performance and scalability by designing backend architecture and optimizing database schemas and SQL queries, resulting in faster data retrieval and reduced response time.', 
        'Enhanced system reliability by implementing authentication, input validation, and structured error handling, reducing potential system failures and improving API robustness.', 
        'Golang (Fiber), GORM, PostgreSQL, Redis, Docker'
      ]
    },
    {
      company: 'Binus Online',
      role: 'Laboratory Assistant - Computational & Programming for Data Science',
      period: 'July 2025 - Present',
      logo: '/images/binus.png',
      responsibilities: [
        'Facilitated practicum sessions for Computing and Programming for Data Science cluster (CS005)',
        'Delivered course materials through lectures, live coding demonstrations',
        'Assessed and graded assignments with constructive feedback',
        'Handled following lab courses: Computational Statistics (July-Present), Algorithm and Programming (October - Present)'
      ]
    },
    {
      company: 'University of Indonesia',
      role: 'Teaching Assistant - Advanced Statistics',
      period: 'February 2025 - June 2025',
      logo: '/images/makara.png',
      responsibilities: [
        'Assisted students in inferential statistics, Chi-square, Regression, time series',
        'Developed comprehensive tutorials on R programming',
        'Evaluated assignments and provided feedback'
      ]
    },
    {
      company: 'PT Bank Syariah Indonesia',
      role: 'Data Decision Management Intern',
      period: 'May 2024 - August 2024',
      logo: '/images/bsi.png',
      responsibilities: [
        'Enabled automated sentiment analysis of user reviews by developing an end-to-end NLP-based web system, improving the efficiency of identifying customer issues in BSI Mobile.',
        'Built scalable data pipelines by implementing scraping, preprocessing, and integration processes, enabling structured data flow for downstream machine learning tasks.',
        'Improved system scalability by designing batch processing and ML pipeline architecture, enabling near real-time prediction and efficient data processing.', 
        'Python (Streamlit), Tensorflow, Scikit-Learn, MySQL'
      ]
    },
    {
      company: 'Bangkit Academy',
      role: 'Machine Learning Cohort',
      period: 'February 2024 - July 2024',
      logo: '/images/bangkit.jpeg',
      responsibilities: [
        'Completed ML training covering algorithms and data visualization',
        'Built financial classification system using NLP',
        'Deployed web application for financial record monitoring'
      ]
    },
    {
      company: 'Xeratic',
      role: 'Data Engineer Intern',
      period: 'September 2022 - November 2022',
      logo: '/images/xeratic.png',
      responsibilities: [
        'Transformed raw data into analytics-ready datasets by designing and implementing batch ETL pipelines using Pentaho, enabling efficient data analysis and reporting.',
        'Improved data processing performance by optimizing SQL queries, resulting in faster data loading and more efficient reporting workflows',
        'Supported data-driven decision making by collaborating with analytics teams to deliver Tableau dashboards built on curated datasets.', 
        'Pentaho, PostgreSQL, Tableau'
      ]
    }
  ];

  const projects = [
    { title: 'Logisfy: Manage Delivery Operations With Confidence', org: 'PT Technology Data Nusantara', image: '/images/logisfy.png' },
    { title: 'NLP Sentiment & LDA Analysis', org: 'PT Bank Syariah Indonesia', image: '/images/project_nlp_bsi.png' },
    { title: 'Automation Generating P2TL', org: 'UP3 Menteng', image: '/images/p2tl.png' },
    { title: 'Financial Track', org: 'Bangkit Academy Capstone', image: '/images/ekspensi.png' },
    { title: 'PeacePath: Navigate with Ease', org: 'AI Competition Umrah', image: '/images/peacePath.png' },
    { title: 'PANDAWA - Eye Disease Detection', org: 'TSDN 2024', image: '/images/tsdn.png' },
    { title: 'SahihAI: Integrated Worship Assistant', org: 'MTQ Desain Aplikasi', image: '/images/sahihAI.png' },
    { title: 'LacaKas: Every Receh Counts', org: 'Korea Asean Digital Academy II 2025', image: '/images/lacakas.png' }
  ];

  const achievements = [
    { title: 'Dev Certified for Machine Learning with TensorFlow', link: 'https://dev.id/certificate/verify/KRW2JPGWND' },
    { title: 'Third Runner-up MTQMN Desain Aplikasi Alquran', link: 'https://drive.google.com/file/d/1f4dH1llLNht0fgbCe5_oTLGHwetPo9o4/view?usp=sharing' },
    { title: '3rd Place Regression Rumble NDC 2025: Advanced Ocean Data Regression Challenge', link: 'https://drive.google.com/file/d/1K7pWPmVKunxcMz_Ro3Sl4y8_6Yv1N8DU/view?usp=sharing' },
    { title: 'Semifinalist Statistics Analysis Competition (SAC) Gammafest 2024', link: 'https://drive.google.com/file/d/14xjIRDjhTv1yP48kBBwxzQ-O1X1uuqzm/view?usp=sharing' },
    { title: '2nd Place in Data Analytics Competition Pesta Data Nasional FST UIN Jakarta 2023', link: 'https://drive.google.com/file/d/1gEY6PW4cgjogSRD5HB-2e7x1XGH6xacI/view?usp=sharing' },
    { title: 'Awardee and Top Achiever Tetris Batch 2 Data Analytics Scholarship from DQLab', link: 'https://drive.google.com/file/d/1ksEMhIC1Y5nBZt6pjXCRFXXzWbgitRdj/view?usp=sharing' }
  ];

  return (
    <div className="portfolio">
      <div className="background-grid"></div>

      {/* Sidebar Navigation */}
      <aside className={`sidebar ${isMenuOpen ? 'open' : ''}`}>
        <div className="sidebar-content">
          <div className="sidebar-header">
            <span className="logo">Ludy Hasby Aulia</span>
            <button onClick={() => setIsMenuOpen(!isMenuOpen)} className="menu-toggle">
              {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>

          <nav className="nav-menu">
            {navItems.map((item) => (
              <button
                key={item.id}
                onClick={() => scrollToSection(item.id)}
                className={`nav-item ${activeSection === item.id ? 'active' : ''}`}
              >
                <span className="nav-icon">{item.icon}</span>
                <span className="nav-label">{item.label}</span>
              </button>
            ))}
          </nav>

          <div className="sidebar-footer">
            <div className="social-links">
              <a href="https://github.com/ludyhasby" target="_blank" rel="noopener noreferrer">
                <Github size={24} />
              </a>
              <a href="https://kaggle.com/ludyhasby" target="_blank" rel="noopener noreferrer">
                <Code size={24} />
              </a>
              <a href="https://www.linkedin.com/in/ludy-hasby/" target="_blank" rel="noopener noreferrer">
                <Linkedin size={24} />
              </a>
              <a href="mailto:ludy.hasby@gmail.com">
                <Mail size={24} />
              </a>
            </div>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className={`main-content ${isMenuOpen ? 'shifted' : ''}`}>
        {/* About Section */}
        <section id="about" className="section">
          <div className="container">
            <div className="code-greeting">
              <div className="code-line">
                <span className="code-keyword">std::cout</span>
                <span className="code-operator"> &lt;&lt; </span>
                <span className="code-string">"</span>
                <div className="greeting-animation">
                  <div className="greeting-wrapper" style={{ transform: `translateY(-${codeText * 33.33}%)` }}>
                    <div className="greeting greeting-1">{greetings[0]}</div>
                    <div className="greeting greeting-2">{greetings[1]}</div>
                    <div className="greeting greeting-3">{greetings[2]}</div>
                  </div>
                </div>
                <span className="code-string">"</span>
                <span className="code-operator"> &lt;&lt; </span>
                <span className="code-keyword">std::endl;</span>
              </div>
            </div>

            <div className="intro-box">
              <h1 className="title">Backend Developer</h1>
            </div>

            <div className="about-grid">
              <div className="about-image">
                <img src="/test.png" alt="Ludy Hasby" className="profile-picture" />
              </div>
              <div className="about-text">
                <p>👋🏻 Hi, I'm Ludy! A backend developer with hands-on experience in machine learning, analytics, and backend engineering.</p>
                <p>💼 I’m passionate about building end-to-end solutions that combine data intelligence with robust software development.</p>
                <p>👨🏼‍💻 <strong>Interests:</strong> ML Engineering, Full-Stack Development, NLP, Data Engineering.</p>
                <p>🚀 <strong>Goal:</strong> To grow as a developer who can build scalable data-driven products.</p>
              </div>
            </div>
          </div>
        </section>

        {/* Experience Section */}
        <section id="experience" className="section section-alt">
          <div className="container">
            <h2 className="section-title">Experience</h2>
            <div className="experience-list">
              {experiences.map((exp, idx) => (
                <div key={idx} className="experience-card">
                  <img src={exp.logo} alt={exp.company} className="exp-logo" />
                  <div className="exp-content">
                    <h3 className="exp-role">{exp.role}</h3>
                    <p className="exp-company">{exp.company}</p>
                    <p className="exp-period">{exp.period}</p>
                    <ul className="exp-responsibilities">
                      {exp.responsibilities.map((resp, i) => (
                        <li key={i}>{resp}</li>
                      ))}
                    </ul>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Skills Section */}
        <section id="skills" className="section">
          <div className="container">
            <h2 className="section-title">Technical Skills</h2>
            <div className="skills-grid">
              <div className="skill-card">
                <h3>Programming Languages</h3>
                <p>Golang, Python, Javascript, SQL, C++, C, R, Java, Stata</p>
              </div>
              <div className="skill-card">
                <h3>Frameworks</h3>
                <p>Go Fiber, Express, Flask, React, TensorFlow, PyTorch, Streamlit, Keras, Scikit-learn, Django</p>
              </div>
              <div className="skill-card">
                <h3>Database Systems</h3>
                <p>PostgreSQL, MongoDB, MySQL, SQLite</p>
              </div>
              <div className="skill-card">
                <h3>Tools</h3>
                <p>Docker, EC2, DigitalOcean, DBT, Polars, Pentaho</p>
              </div>
              <div className="skill-card skill-card-wide">
                <h3>Data Science Techniques</h3>
                <p>Regression, Classification, Clustering, NLP, Computer Vision, Recommendation System</p>
                <p>Decision Tree, Random Forest, XGBoost, CatBoost, Ensemble Methods</p>
              </div>
            </div>
          </div>
        </section>

        {/* Education Section */}
        <section id="education" className="section section-alt">
          <div className="container">
            <h2 className="section-title">Education</h2>
            <div className="education-list">
              <div className="education-card">
                <img src="/images/binus.png" alt="Binus" className="edu-icon" />
                <div className="edu-content">
                  <h3>Bachelor of Computer Science</h3>
                  <p className="edu-school">University of Bina Nusantara, Online Learning</p>
                  <p className="edu-period">2023 - 2027 | GPA: 4.0/4.0</p>
                  <p className="edu-courses">Coursework: Algorithm and Programming, Data Structures, Database, Linear Algebra</p>
                </div>
              </div>
              <div className="education-card">
                <img src="/images/makara.png" alt="UI" className="edu-icon" />
                <div className="edu-content">
                  <h3>Bachelor of Economics</h3>
                  <p className="edu-school">University of Indonesia, Depok</p>
                  <p className="edu-period">2021 - 2025 | GPA: 3.89/4.0</p>
                  <p className="edu-courses">Coursework: Microeconomics, Industrial Economics, Capital Market Investment</p>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Projects Section */}
        <section id="projects" className="section">
          <div className="container">
            <h2 className="section-title">Projects</h2>
            <div className="projects-grid">
              {projects.map((project, idx) => (
                <div key={idx} className="project-card">
                  <div className="project-image">
                    <img src={project.image} alt={project.title} />
                  </div>
                  <div className="project-info">
                    <h3>{project.title}</h3>
                    <p>{project.org}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Achievement Section */}
        <section id="achievement" className="section section-alt">
          <div className="container">
            <h2 className="section-title">Achievements</h2>
            <div className="achievement-list">
              {achievements.map((achievement, idx) => (
                <div key={idx} className="achievement-card">
                  <Award className="achievement-icon" size={32} />
                  <div className="achievement-content">
                    <p>{achievement.title}</p>
                  </div>
                  {achievement.link !== '#' && (
                    <a href={achievement.link} target="_blank" rel="noopener noreferrer" className="achievement-link">
                      <ExternalLink size={20} />
                    </a>
                  )}
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Contact Section */}
        <section id="contacts" className="section">
          <div className="container contact-container">
            <h2 className="section-title">Let's Connect</h2>
            <p className="contact-text">
              You may reach out to me at <a href="mailto:ludy.hasby@gmail.com">ludy.hasby@gmail.com</a>
            </p>
            
            <div className="contact-grid">
              <div className="contact-card">
                <h3>Open to Opportunities</h3>
                <ul>
                  <li>Freelance & Contract Work</li>
                  <li>Mentoring</li>
                  <li>Competition Collaborate</li>
                  <li>Data & ML Processing Work</li>
                </ul>
              </div>
              <div className="contact-card">
                <h3>Current Work</h3>
                <ul>
                  <li>Logisfy Phase 3</li>
                  <li>Golang Developer</li>
                </ul>
              </div>
            </div>

            <div className="social-links-large">
              <a href="https://github.com/ludyhasby" target="_blank" rel="noopener noreferrer">
                <Github size={32} />
              </a>
              <a href="https://kaggle.com/ludyhasby" target="_blank" rel="noopener noreferrer">
                <Code size={32} />
              </a>
              <a href="https://www.linkedin.com/in/ludy-hasby/" target="_blank" rel="noopener noreferrer">
                <Linkedin size={32} />
              </a>
              <a href="mailto:ludy.hasby@gmail.com">
                <Mail size={32} />
              </a>
            </div>

            <p className="footer">Copyright © 2025 Ludy Hasby</p>
          </div>
        </section>
      </main>

      {isMenuOpen && <div className="overlay" onClick={() => setIsMenuOpen(false)}></div>}
    </div>
  );
}