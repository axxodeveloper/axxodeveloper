from components import Heading, Value, TimeElapsed, Separator, WorkingOn, CommitGraph, GithubStats, Last24Hr, CurrentDate

# Layout configuration for your profile README neofetch layout

Heading("ΛXXӨ@GitHub", CurrentDate())
Value("OS", "Windows 10, Linux (Kali)")
TimeElapsed("Uptime", 2008, 11, 9) # Customize or keep as a baseline
Value("IDE", "VSCode, Cursor, Claude")
Value("Status", "Learning & Building")
Separator()
WorkingOn()
Separator()
Value("Languages.Programming", "Python, Bash, JavaScript, C#")
Value("Languages.Real", "English, Sinhala, Tamil")
Separator()
Value("Hobbies.Software", "Cybersecurity, Web-Dev, Hacking")
Value("Hobbies.Hardware", "PC Troubleshooting, Networking, Robotics, Raspberry pi")
Separator()
Heading("Contact")
Value("Email", "axxo.vibercoder@gmail.com")
Value("GitHub", "github.com/axxodeveloper")
Separator()
GithubStats("Repos", "Stars", "Commits", "Followers", "Pull.Requests", "Lines.of.Code")
Separator()
CommitGraph()
Last24Hr("Pushes", "Pull.Requests", "Issues", "Starred", "Forked", "Releases", "Reviewed", "Comments")
