"""All site copy and data. Edit here, then run `python3 build/build.py`.

Truth rules: every resource URL was checked live on 2026-09-29, every video ID is a
public upload on @collegeconversations, and every number is from the channel's own
analytics (2026-09-16 snapshot) or the resource's own site. Nothing is invented.
"""

CHECKED = "September 2026"
SITE_URL = "https://collegeconversations.org/"
CHANNEL = "https://www.youtube.com/@collegeconversations"
SUBSCRIBE = CHANNEL + "?sub_confirmation=1"

# key: (youtube id, title as published, duration)
VIDEOS = {
    "credit":        ("J5bFRxpCnos", "Understanding Credit Hours", "4:48"),
    "credit60":      ("Mx7To0ytLCA", "Credit Hour Explained In Under 60 Seconds", "1:00"),
    "creditq":       ("BwGsLTYMBrQ", "Your Credit Hour Question Finally Answered", "9:57"),
    "creditmath":    ("ZQ6rAbcCLDc", "Credit Hours Simplified: Breaking Down the Math", "1:42"),
    "fifteen":       ("SjWk-Brqd9k", "Is 15 Credits Too Much? What College Students Should Know", "4:18"),
    "howmany":       ("u_pd_zMuDsA", "How Many Classes Should You Take In College?", "2:50"),
    "transfer":      ("ZzAncZ2NpSM", "3 Reasons Your Credits Didn't Transfer", "4:31"),
    "collegelist":   ("fzGbgtYk8NM", "How to Build a College List (That Gets You Choices)", "7:54"),
    "essay":         ("gv_89vwYZVc", "The #1 College Essay Mistake (And the 3-Step Fix)", "8:58"),
    "admissions":    ("2VSMKXTr0X4", "What Admissions Officers Actually Look For (5 Factors)", "8:24"),
    "freshman":      ("imzsVsy7Wa4", "What I Wish You Knew Before Freshman Year", "10:40"),
    "roadmap":       ("QiXcZSwCqlM", "How To Survive Your First Semester Of College: A Roadmap", "6:40"),
    "before5":       ("u7mei_O7D6E", "5 Things You Must Know Before Starting College", "7:30"),
    "ai":            ("Cm--1bGjhEg", "College + AI: What Your Syllabus Actually Says", "7:16"),
    "profs":         ("m9ZxVqex33s", "5 Things Professors Wish Every Student Knew", "7:56"),
    "notice":        ("NnZe1asXlq8", "What Professors Notice About Students", "4:43"),
    "group":         ("E5eJxp0l9X0", "How to Get an A on Group Projects in College", "5:45"),
    "internship":    ("S3IIQ-PhbiY", "How to Find an Internship", "7:01"),
    "advisor":       ("_07qYSsGaF4", "How to Meet with an Academic Advisor", "5:28"),
    "advisorfail":   ("gsxwdogGXGc", "Your Academic Advisor Appointments Don't Have to Fail", "4:25"),
    "ungrading":     ("1TSEZ6cQwW8", "What Ungrading Means for Your College GPA", "4:21"),
    "evals":         ("hLhHH4VZSM4", "Course Evaluations, Don't Get This Wrong", "8:50"),
    "involvement":   ("AfB4PHP3hSw", "Student Involvement That Doesn't Destroy Your Future", "9:28"),
    "gapyear":       ("DBKF9bUJEgA", "The Gap Year Question Every Student Asks", "8:11"),
    "moneymistake":  ("9xKZUwxIRPw", "The Money Mistake Every College Student Makes", "8:00"),
    "cheating":      ("hDsjlsKF_V8", "You May Not Know You're Cheating", "12:27"),
    "planning":      ("kAX8iZsJjj4", "Planning Doesn't Have to Be Stressful", "8:16"),
    "chatgpt":       ("4F74BQKqlOc", "Is ChatGPT Making Students Lazy? What Experts Say", "15:17"),
    "finalyear":     ("HV4CXnRWxmw", "Graduating Soon? Here's Your Final Year Roadmap", "3:52"),
    "purpose":       ("hVgTIdD_200", "Why Most Students Never Find Their Purpose", "14:23"),
    "capstone":      ("IQqa9zXoV4M", "How to Pass Your Capstone Course", "3:48"),
    "prereq":        ("GFVp1NJuVH4", "What are Prerequisites?", "2:56"),
    "degreeplan":    ("-2crdJZepY4", "The 3 Components Every Student Needs to Know About Degree Plans", "3:57"),
    "electives":     ("t9Ucwu6owNo", "These Elective Courses Work for Any Major", "4:59"),
    "free5":         ("BWrggAht-P0", "5 Free Resources That Make College More Affordable", "4:36"),
    "paidfor":       ("GDapEGwQeko", "College Paid For These: Why Aren't You Using Them?", "4:56"),
    "changing":      ("eVg7qyfdG_I", "Changing Majors But Still Graduating", "6:06"),
    "rightmajor":    ("tHtcf0tg0qU", "Five Signs You're in the Right Major", "5:51"),
    "wrongmajor":    ("vL8EC6L6OTE", "Worried You're in the Wrong Major?", "3:46"),
    "dontteach":     ("7bWE1dyNqzs", "What They Don't Teach You In College", "3:18"),
    "fys":           ("7K0Kkcll3_0", "What is A First Year Seminar?", "5:59"),
    "syllabus":      ("S7uv0wx2VKE", "What is a College Syllabus?", "5:16"),
    "accreditation": ("ZQSlcTVQxFI", "Why School Accreditation is Important", "5:27"),
    "careerfair":    ("gyiF7uRdH50", "3 Quick Tips On Attending A Career Fair", "0:56"),
    "burnout":       ("QrIGBKXFr4k", "How to Bounce Back from Burnout", "11:35"),
}

# Video shelf tabs (first entry of "start" is the featured video)
SHELVES = [
    ("start", "Start here", ["roadmap", "degreeplan", "electives", "profs", "freshman", "advisor"]),
    ("machinery", "How college works", ["prereq", "syllabus", "fys", "capstone", "accreditation", "transfer"]),
    ("apply", "Getting in", ["collegelist", "admissions", "essay", "gapyear", "before5", "planning"]),
    ("money", "Money", ["paidfor", "free5", "moneymistake", "fifteen", "howmany", "creditq"]),
    ("grades", "Classes and grades", ["notice", "group", "ai", "cheating", "ungrading", "evals"]),
    ("after", "Majors and careers", ["changing", "rightmajor", "internship", "finalyear", "dontteach", "purpose"]),
]

STAGES = {"before": "Before college", "during": "In college", "after": "After college"}

CATEGORIES = [
    ("apply", "Choosing and applying", "Find schools that fit, apply once and compare what they really cost."),
    ("credit", "Tests and college credit", "The exams, and every way to walk in with credit already earned."),
    ("money", "Paying for college", "Federal aid, scholarships and the forms that unlock them."),
    ("study", "Studying and writing", "Free tools for notes, research, citations and remembering what you study."),
    ("perks", "Free software and courses", "What your student email already gets you."),
    ("career", "Careers and internships", "Figure out what jobs exist, what they pay and how to get in."),
    ("after", "After graduation", "Grad school tests, service years and paying back loans."),
    ("health", "Health and crisis support", "Free, confidential and there at 3 a.m."),
    ("needs", "Food, housing and basic needs", "Help that many students qualify for and never ask about."),
    ("access", "First-gen, access and your rights", "For first-generation students, students with disabilities and the people helping them."),
]

# price labels: "Government" = official .gov, free; others describe cost honestly.
R = []
def res(cat, name, org, url, desc, price, stages, video=None):
    R.append(dict(cat=cat, name=name, org=org, url=url, desc=desc, price=price, stages=stages, video=video))

# --- Choosing and applying
res("apply", "Common App", "Common App", "https://www.commonapp.org/",
    "One application you can send to more than 1,000 colleges. Free to use; some colleges charge an application fee, and fee waivers exist.",
    "Free to use", ["before"], "collegelist")
res("apply", "BigFuture", "College Board", "https://bigfuture.collegeboard.org/",
    "Search colleges, explore majors and careers, and find scholarships in one place.",
    "Free", ["before"])
res("apply", "College Scorecard", "U.S. Department of Education", "https://collegescorecard.ed.gov/",
    "Compare colleges on graduation rates, average cost after aid and what graduates go on to earn.",
    "Government", ["before"])
res("apply", "College Navigator", "National Center for Education Statistics", "https://nces.ed.gov/collegenavigator/",
    "Official federal data on thousands of colleges: tuition, enrollment, retention and graduation rates.",
    "Government", ["before"])
res("apply", "Net Price Calculator Center", "U.S. Department of Education", "https://collegecost.ed.gov/net-price",
    "Find any college's net price calculator and estimate what you would actually pay, not the sticker price.",
    "Government", ["before"])
res("apply", "QuestBridge", "QuestBridge", "https://www.questbridge.org/",
    "Connects high-achieving students from low-income backgrounds with full four-year scholarships at partner colleges.",
    "Free", ["before"])

# --- Tests and credit
res("credit", "Bluebook", "College Board", "https://bluebook.collegeboard.org/",
    "The official testing app for the digital SAT and PSAT, with full-length practice tests you can take for free.",
    "Free practice", ["before"])
res("credit", "ACT", "ACT", "https://www.act.org/",
    "Register for the ACT and find official prep materials, including a free practice test.",
    "Exam fee", ["before"])
res("credit", "AP Credit Policy Search", "College Board", "https://apstudents.collegeboard.org/getting-credit-placement/search-policies",
    "Look up how much credit a college gives for each AP exam and score before you choose where to send them.",
    "Free", ["before"])
res("credit", "CLEP", "College Board", "https://clep.collegeboard.org/",
    "Earn college credit for what you already know by passing one exam, at colleges that accept CLEP.",
    "Exam fee", ["before", "during"])
res("credit", "Transferology", "Transferology", "https://www.transferology.com/",
    "See how your courses and exam credit would transfer to another college before you move.",
    "Free", ["during"], "transfer")

# --- Paying for college
res("money", "FAFSA", "Federal Student Aid", "https://studentaid.gov/h/apply-for-aid/fafsa",
    "The form for federal grants, work-study and loans, and most states and colleges use it too. File it every year, and never pay anyone to file it.",
    "Government", ["before", "during"], "paidfor")
res("money", "Federal Student Aid Estimator", "Federal Student Aid", "https://studentaid.gov/aid-estimator/",
    "Estimate your Student Aid Index and Pell Grant eligibility before you file.",
    "Government", ["before"])
res("money", "CSS Profile", "College Board", "https://cssprofile.collegeboard.org/",
    "A second aid application some private colleges require before they award their own grants. Check each school's list.",
    "Fee, waivers available", ["before"])
res("money", "Federal Pell Grant", "Federal Student Aid", "https://studentaid.gov/understand-aid/types/grants/pell",
    "Federal grant money for undergraduates with financial need. It usually doesn't have to be repaid.",
    "Government", ["before", "during"])
res("money", "Federal Work-Study", "Federal Student Aid", "https://studentaid.gov/understand-aid/types/work-study",
    "Part-time jobs for students with financial need, often on campus and flexible around classes.",
    "Government", ["during"])
res("money", "Subsidized and unsubsidized loans", "Federal Student Aid", "https://studentaid.gov/understand-aid/types/loans/subsidized-unsubsidized",
    "How federal Direct Loans work, and why the government pays the interest on subsidized loans while you're enrolled at least half-time.",
    "Government", ["before", "during"])
res("money", "Understanding your aid offer", "Federal Student Aid", "https://studentaid.gov/resources/aid-offer",
    "How to read an aid offer line by line, compare offers and tell a grant from a loan.",
    "Government", ["before"])
res("money", "Scholarship Finder", "CareerOneStop, U.S. Department of Labor", "https://www.careeronestop.org/Toolkit/Training/find-scholarships.aspx",
    "A free scholarship search sponsored by the U.S. Department of Labor, filterable by level, state and field.",
    "Government", ["before", "during"])
res("money", "Fastweb", "Fastweb", "https://www.fastweb.com/",
    "A long-running free scholarship search. A real scholarship never asks you to pay to apply.",
    "Free", ["before", "during"])
res("money", "Paying for College", "Consumer Financial Protection Bureau", "https://www.consumerfinance.gov/paying-for-college/",
    "Compare financial aid offers and plan how you'll cover the rest, from the federal consumer watchdog.",
    "Government", ["before"])
res("money", "Education tax credits", "Internal Revenue Service", "https://www.irs.gov/credits-deductions/individuals/education-credits-aotc-llc",
    "The American Opportunity and Lifetime Learning credits can lower the tax your family owes for tuition paid.",
    "Government", ["before", "during"])
res("money", "GI Bill and VA education benefits", "U.S. Department of Veterans Affairs", "https://www.va.gov/education/",
    "Education benefits for veterans, service members and eligible family members.",
    "Government", ["before", "during"])

# --- Studying and writing
res("study", "Purdue OWL", "Purdue University", "https://owl.purdue.edu/",
    "Clear guides to writing, grammar and citation styles like APA, MLA and Chicago.",
    "Free", ["during"])
res("study", "Zotero", "Zotero", "https://www.zotero.org/",
    "Open-source tool that saves your sources as you research and formats citations and bibliographies for you.",
    "Free", ["during"])
res("study", "Google Scholar", "Google", "https://scholar.google.com/",
    "Search scholarly articles, theses and books, and see who has cited them since.",
    "Free", ["during", "after"])
res("study", "WorldCat", "OCLC", "https://search.worldcat.org/",
    "Search library collections worldwide and find the nearest library that holds a book.",
    "Free", ["during"])
res("study", "The Learning Scientists", "The Learning Scientists", "https://www.learningscientists.org/",
    "Study strategies backed by cognitive science, like retrieval practice and spacing, with free downloadable guides.",
    "Free", ["during"])
res("study", "Anki", "Anki", "https://apps.ankiweb.net/",
    "Flashcards built on spaced repetition, so you review each card right before you'd forget it.",
    "Free on desktop", ["during"])
res("study", "Khan Academy", "Khan Academy", "https://www.khanacademy.org/",
    "Free lessons and practice in math, science, economics and more. Good for filling gaps before a course starts.",
    "Free", ["before", "during"])
res("study", "MIT OpenCourseWare", "Massachusetts Institute of Technology", "https://ocw.mit.edu/",
    "Lecture notes, problem sets, exams and videos from real MIT courses.",
    "Free", ["during"])
res("study", "Crash Course", "Crash Course on YouTube", "https://www.youtube.com/@crashcourse",
    "Fast, well-made video courses on history, science, economics, psychology and more.",
    "Free", ["before", "during"])
res("study", "OpenStax", "Rice University", "https://openstax.org/",
    "Peer-reviewed textbooks for common intro courses, free online. Ask whether your professor accepts them.",
    "Free", ["during"], "free5")
res("study", "LibreTexts", "LibreTexts", "https://libretexts.org/",
    "Open textbooks across nearly every subject, free to read online.",
    "Free", ["during"])
res("study", "Desmos", "Desmos", "https://www.desmos.com/calculator",
    "Graphing and scientific calculators that run in your browser.",
    "Free", ["during"])
res("study", "Wolfram|Alpha", "Wolfram Research", "https://www.wolframalpha.com/",
    "Computes answers to math, science and statistics questions. Step-by-step solutions need a paid plan.",
    "Free tier", ["during"])
res("study", "Hemingway Editor", "Hemingway", "https://hemingwayapp.com/",
    "Highlights long, hard-to-read sentences so your writing gets clearer.",
    "Free on the web", ["during"])
res("study", "Pomofocus", "Pomofocus", "https://pomofocus.io/",
    "A simple Pomodoro timer: focused work blocks with short breaks built in.",
    "Free tier", ["during"])

# --- Free software and courses
res("perks", "GitHub Student Developer Pack", "GitHub", "https://education.github.com/pack",
    "Free developer tools and cloud credits for verified students.",
    "Free for students", ["during"])
res("perks", "Microsoft 365 Education", "Microsoft", "https://www.microsoft.com/en-us/education/products/office",
    "Word, Excel, PowerPoint and OneNote at no cost with a valid school email at eligible schools.",
    "Free for students", ["during"])
res("perks", "Coursera", "Coursera", "https://www.coursera.org/",
    "Online courses from universities and companies. Some content is free; certificates cost money.",
    "Free tier", ["during", "after"])
res("perks", "edX", "edX", "https://www.edx.org/",
    "Courses from universities including Harvard and MIT. Many can be audited for free; certificates cost money.",
    "Free tier", ["during", "after"])

# --- Careers and internships
res("career", "Handshake", "Handshake", "https://joinhandshake.com/",
    "The job and internship platform many colleges use. Sign in through your school to see who recruits there.",
    "Free for students", ["during", "after"], "internship")
res("career", "Occupational Outlook Handbook", "U.S. Bureau of Labor Statistics", "https://www.bls.gov/ooh/",
    "What hundreds of jobs pay, the training they need and how fast they're growing.",
    "Government", ["before", "during"])
res("career", "O*NET OnLine", "U.S. Department of Labor", "https://www.onetonline.org/",
    "Detailed profiles of occupations: daily tasks, skills, education and wages.",
    "Government", ["during"])
res("career", "My Next Move", "U.S. Department of Labor", "https://www.mynextmove.org/",
    "A short interest quiz that suggests careers to explore, with pay and outlook for each.",
    "Government", ["before", "during"])
res("career", "CareerOneStop", "U.S. Department of Labor", "https://www.careeronestop.org/",
    "The Department of Labor's hub for career exploration, training programs and job search.",
    "Government", ["during", "after"])
res("career", "LinkedIn", "LinkedIn", "https://www.linkedin.com/",
    "Build a profile recruiters can find, and use it to reach alumni from your school.",
    "Free tier", ["during", "after"])
res("career", "Pathways for students and graduates", "USAJOBS", "https://www.usajobs.gov/help/working-in-government/unique-hiring-paths/students/",
    "Federal internships and jobs set aside for current students and recent graduates.",
    "Government", ["during", "after"])
res("career", "Idealist", "Idealist", "https://www.idealist.org/",
    "Jobs, internships and volunteer roles at nonprofits.",
    "Free", ["during", "after"])

# --- After graduation
res("after", "Repaying federal loans", "Federal Student Aid", "https://studentaid.gov/manage-loans/repayment",
    "When payments start, the repayment plans on offer and what to do if you can't pay.",
    "Government", ["after"])
res("after", "Public Service Loan Forgiveness", "Federal Student Aid", "https://studentaid.gov/manage-loans/forgiveness-cancellation/public-service",
    "Forgives the remaining balance on eligible federal loans after 120 qualifying payments while working full-time for government or a qualifying nonprofit.",
    "Government", ["after"])
res("after", "GRE General Test", "ETS", "https://www.ets.org/gre.html",
    "The admissions test many graduate and business programs accept.",
    "Exam fee", ["after"])
res("after", "LSAC", "Law School Admission Council", "https://www.lsac.org/",
    "Register for the LSAT and apply to law schools.",
    "Exam fee", ["after"])
res("after", "MCAT", "Association of American Medical Colleges", "https://www.mcat.org/",
    "Everything about the medical school admissions test, from registration to prep.",
    "Exam fee", ["after"])
res("after", "Fulbright U.S. Student Program", "U.S. Department of State", "https://us.fulbrightonline.org/",
    "Grants for graduating seniors and recent graduates to study, research or teach English abroad.",
    "Government", ["after"])
res("after", "AmeriCorps", "AmeriCorps", "https://americorps.gov/",
    "Paid national service. Finishing a term can earn a Segal Education Award for tuition or student loans.",
    "Government", ["after"])
res("after", "Peace Corps", "Peace Corps", "https://www.peacecorps.gov/",
    "Serve abroad in education, health, agriculture and more, usually for 27 months including training.",
    "Government", ["after"])

# --- Health and crisis support
res("health", "988 Suicide & Crisis Lifeline", "988 Lifeline", "https://988lifeline.org/",
    "Call or text 988 any time for free, confidential support from a trained counselor.",
    "Free, 24/7", ["before", "during", "after"])
res("health", "Crisis Text Line", "Crisis Text Line", "https://www.crisistextline.org/",
    "Text HOME to 741741 to reach a trained volunteer crisis counselor.",
    "Free, 24/7", ["before", "during", "after"])
res("health", "The Trevor Project", "The Trevor Project", "https://www.thetrevorproject.org/",
    "Crisis support for LGBTQ+ young people by phone, text and chat.",
    "Free, 24/7", ["before", "during", "after"])
res("health", "SAMHSA National Helpline", "Substance Abuse and Mental Health Services Administration", "https://www.samhsa.gov/find-help/helplines/national-helpline",
    "1-800-662-4357. Confidential treatment referral and information for mental health and substance use.",
    "Free, 24/7", ["before", "during", "after"])
res("health", "RAINN", "RAINN", "https://rainn.org/",
    "The National Sexual Assault Hotline, 1-800-656-4673, or chat online.",
    "Free, 24/7", ["before", "during", "after"])
res("health", "The Jed Foundation", "The Jed Foundation", "https://jedfoundation.org/",
    "Mental health guides for students and families, including how to help a friend who's struggling.",
    "Free", ["before", "during"], "burnout")
res("health", "Active Minds", "Active Minds", "https://www.activeminds.org/",
    "Student-run mental health chapters on campuses across the country.",
    "Free", ["during"])

# --- Basic needs
res("needs", "211", "United Way", "https://www.211.org/",
    "Call 211 or search online to find local help with food, housing, utility bills and more.",
    "Free", ["before", "during", "after"])
res("needs", "SNAP for college students", "U.S. Department of Agriculture", "https://www.fns.usda.gov/snap/students",
    "Some college students qualify for SNAP food benefits. See the student rules and the exemptions.",
    "Government", ["during"])
res("needs", "Swipe Out Hunger", "Swipe Out Hunger", "https://swipehunger.org/",
    "The national nonprofit fighting student hunger. Many campuses run a pantry or meal-swipe sharing; ask your dean of students.",
    "Free", ["during"])

# --- First-gen, access and rights
res("access", "I'm First!", "Strive for College", "https://www.imfirst.org/",
    "Guidance and real stories from and for first-generation college students.",
    "Free", ["before", "during"])
res("access", "FirstGen Forward", "FirstGen Forward", "https://www.firstgenforward.org/",
    "The national center focused on first-generation college student success.",
    "Free", ["before", "during"])
res("access", "Understood", "Understood", "https://www.understood.org/",
    "Help for people who learn and think differently, including ADHD and dyslexia, and how accommodations work.",
    "Free", ["before", "during"])
res("access", "Disability rights under the ADA", "U.S. Department of Justice", "https://www.ada.gov/topics/intro-to-ada/",
    "Your rights under the Americans with Disabilities Act. At college, accommodations start with the disability services office.",
    "Government", ["before", "during"])
res("access", "FERPA: who sees your records", "U.S. Department of Education", "https://studentprivacy.ed.gov/faq/what-ferpa",
    "In college, the rights to your education records are yours. Parents generally need your consent to see grades.",
    "Government", ["during"])
res("access", "Check a school's accreditation", "U.S. Department of Education", "https://ope.ed.gov/dapip/",
    "Look up whether a school is accredited by a recognized agency before you enroll or transfer.",
    "Government", ["before", "during"], "accreditation")
res("access", "NCAN", "National College Attainment Network", "https://www.ncan.org/",
    "Resources for counselors, mentors and programs helping students get to and through college.",
    "Free", ["before"])

RESOURCES = R

# --- Roadmap: six stages, each item a checkable task with one link.
# link: ("video", key) or ("url", label, url)
ROADMAP = [
    dict(id="senior", n="01", title="Senior year of high school", when="August to May",
         who="Finishing high school",
         items=[
            ("Build a list of colleges where you'd be happy, with reach, target and likely schools.", ("video", "collegelist")),
            ("Learn what admissions offices weigh, beyond grades and scores.", ("video", "admissions")),
            ("Write an essay only you could have written.", ("video", "essay")),
            ("File the FAFSA as early as you can. Some state and college aid runs out.", ("url", "Open the FAFSA", "https://studentaid.gov/h/apply-for-aid/fafsa")),
            ("Check whether any school on your list also requires the CSS Profile.", ("url", "Check CSS Profile schools", "https://cssprofile.collegeboard.org/")),
            ("Compare every school's net price, not its sticker price.", ("url", "Find net price calculators", "https://collegecost.ed.gov/net-price")),
         ]),
    dict(id="summer", n="02", title="The summer before college", when="May to August",
         who="Starting this fall",
         items=[
            ("Read every line of your aid offer and mark which parts are loans.", ("url", "Read your aid offer", "https://studentaid.gov/resources/aid-offer")),
            ("Understand credit hours before you register for a single class.", ("video", "credit")),
            ("Go to orientation with your questions written down.", ("video", "freshman")),
            ("Look up how your AP, dual-credit or CLEP credit counts.", ("url", "Look up AP credit policies", "https://apstudents.collegeboard.org/getting-credit-placement/search-policies")),
            ("Check for free textbooks before you buy any.", ("url", "Find free textbooks", "https://openstax.org/")),
            ("Know the five things nobody tells you until week one.", ("video", "before5")),
         ]),
    dict(id="first", n="03", title="Your first semester", when="Weeks 1 to 15, then finals",
         who="In your first year",
         items=[
            ("Read every syllabus in week one and put every deadline in one calendar.", ("video", "syllabus")),
            ("Find your add/drop and withdrawal deadlines before you need them.", ("video", "roadmap")),
            ("Go to office hours at least once for every class, even if nothing’s wrong.", ("video", "profs")),
            ("Meet your academic advisor before registration opens for next term.", ("video", "advisor")),
            ("Use what your tuition already pays for: tutoring, the writing center and counseling.", ("video", "paidfor")),
            ("Know your school's rules on AI before you open a chatbot for an assignment.", ("video", "ai")),
         ]),
    dict(id="every", n="04", title="Every semester after", when="Each term",
         who="In college now",
         items=[
            ("Run your degree audit and compare it with your degree plan.", ("video", "degreeplan")),
            ("Check prerequisites before you register, so a sequence doesn't slip.", ("video", "prereq")),
            ("Take enough credits to stay on pace: 120 credits over 8 semesters is 15 a term.", ("video", "fifteen")),
            ("Refile the FAFSA once a year, for every school year you want aid.", ("url", "Open the FAFSA", "https://studentaid.gov/h/apply-for-aid/fafsa")),
            ("Pick electives that build a skill any employer will pay for.", ("video", "electives")),
            ("Fill in your course evaluations. Professors do read them.", ("video", "evals")),
         ]),
    dict(id="final", n="05", title="Your final year", when="The last two terms",
         who="About to graduate",
         items=[
            ("Map your final year: what's left, and when you'll take it.", ("video", "finalyear")),
            ("Apply for graduation by your registrar's deadline.", None),
            ("Plan your capstone early. It's the course that decides your last semester.", ("video", "capstone")),
            ("Get an internship or other work experience in your field.", ("video", "internship")),
            ("Walk into the career fair with three prepared questions.", ("video", "careerfair")),
            ("If you borrowed federal loans, complete exit counseling before you leave.", ("url", "Complete exit counseling", "https://studentaid.gov/exit-counseling/")),
         ]),
    dict(id="afterwards", n="06", title="After graduation", when="Your first year out",
         who="Just graduated",
         items=[
            ("Pick a loan repayment plan before your grace period ends.", ("url", "Compare repayment plans", "https://studentaid.gov/manage-loans/repayment")),
            ("Working for government or a nonprofit? Check Public Service Loan Forgiveness.", ("url", "See if you qualify for PSLF", "https://studentaid.gov/manage-loans/forgiveness-cancellation/public-service")),
            ("Look up what jobs in your field actually pay.", ("url", "Look up pay by job", "https://www.bls.gov/ooh/")),
            ("Considering grad school? Know which test your programs want.", ("url", "Learn about the GRE", "https://www.ets.org/gre.html")),
            ("Learn the skills college didn't teach you.", ("video", "dontteach")),
         ]),
]

PATHS = [
    ("senior", "before", "I'm finishing high school", "Lists, essays, the FAFSA and what it really costs."),
    ("summer", "before", "I start college this fall", "Credit hours, orientation, your aid offer."),
    ("first", "during", "I'm in my first year", "Syllabi, office hours, advisors, deadlines."),
    ("every", "during", "I'm in college now", "Degree audits, prerequisites, staying on pace."),
    ("final", "after", "I'm about to graduate", "Capstones, internships, loans, what's next."),
]

# --- The Decoder: college words nobody explains at orientation
TERMS = [
    ("Credit hour", "The unit colleges use to measure a course. One credit usually means about one hour in class plus about two hours of work outside it, every week of a roughly 15-week semester. Most bachelor's degrees take about 120.", "credit"),
    ("Full-time status", "For undergraduates, usually 12 or more credits a semester. It can affect financial aid, health insurance and housing, so check before you drop a class.", "howmany"),
    ("Prerequisite", "A course you have to pass before you can take another. Miss one and a whole sequence can slip a semester.", "prereq"),
    ("Corequisite", "A course you take at the same time as another, like a lab alongside its lecture.", None),
    ("Degree plan", "The full list of courses your degree requires, usually split into general education, major requirements and electives.", "degreeplan"),
    ("Degree audit", "A report from your school that checks the courses you've finished against your degree plan and shows exactly what's left.", None),
    ("General education", "The core courses every student takes, like writing, math and science, whatever the major. Often called gen eds or the core.", None),
    ("Elective", "A course you choose freely to reach your total credits. The best ones build a skill you'll use anywhere.", "electives"),
    ("Major and minor", "Your major is your main field of study. A minor is a smaller set of courses in a second field.", "rightmajor"),
    ("Syllabus", "The rulebook for a course: grading, deadlines, attendance and policies, including on AI. Read it in week one.", "syllabus"),
    ("Office hours", "Time your professor sets aside to meet students. You don't need a problem to go.", "profs"),
    ("Add/drop period", "The first days of a term when you can change your schedule without a mark on your transcript. Check your school's refund schedule too.", "roadmap"),
    ("Withdrawal (W)", "Leaving a course after add/drop. It usually shows as a W and doesn't count in your GPA, but it can affect aid and your pace to graduate.", None),
    ("Incomplete (I)", "A temporary grade some professors allow when an emergency stops you from finishing. You complete the work by a set deadline.", None),
    ("GPA", "Grade point average. Each grade converts to points (an A is 4.0 on most scales), weighted by the course's credits.", "ungrading"),
    ("Academic probation", "A warning status when your GPA falls below your school's minimum. It comes with a plan and a deadline to recover.", None),
    ("Satisfactory Academic Progress", "The grades and completion pace you must keep to stay eligible for federal financial aid. Usually shortened to SAP.", None),
    ("FAFSA", "The Free Application for Federal Student Aid. It's the form for federal grants, loans and work-study, and most states and colleges use it too.", "paidfor"),
    ("Student Aid Index", "The number the FAFSA calculates from your family's finances to decide what aid you can get. It replaced the EFC starting with the 2024 to 2025 school year.", None),
    ("Cost of attendance", "A college's estimate of a full year: tuition, fees, housing, food, books, transportation and personal costs.", None),
    ("Net price", "What you'd actually pay: cost of attendance minus grants and scholarships. Loans don't lower it; you still owe them.", None),
    ("Grant vs. loan", "Grants and scholarships are gifts you usually don't repay. Loans are borrowed money you repay with interest.", "moneymistake"),
    ("Subsidized loan", "A federal loan for undergraduates with financial need. The government pays the interest while you're enrolled at least half-time.", None),
    ("Work-study", "A federal program that funds part-time jobs for students with financial need.", None),
    ("Registrar", "The office that keeps your academic record: registration, transcripts, grades and graduation.", None),
    ("Bursar", "The office that bills you and takes payments. Some schools call it Student Accounts.", None),
    ("Capstone", "A final course, usually in your last year, where you pull your major together in one big project.", "capstone"),
    ("First-year seminar", "A small course for new students that teaches how college works and connects you with a professor early.", "fys"),
    ("Accreditation", "Outside review that confirms a school meets quality standards. It affects federal aid and whether your credits transfer.", "accreditation"),
    ("Transfer credit", "Credit one school accepts for courses you took at another. Check before you enroll, not after.", "transfer"),
    ("FERPA", "The federal law that gives college students control over their education records, including who can see their grades.", None),
    ("Grace period", "The months after you leave school before federal loan payments start. For Direct Subsidized and Unsubsidized Loans it's six months.", None),
]

MARQUEE = ["Credit hours", "Prerequisites", "The FAFSA", "Degree plans", "Office hours", "Electives",
           "Add/drop", "Capstones", "Accreditation", "Work-study", "Transfer credit", "The syllabus"]

FAQ = [
    ("Is everything here free?",
     "Almost everything is free, and each card says what it costs. A few, like the ACT, GRE and CSS Profile, charge a fee, and most offer waivers if cost is a barrier. A real scholarship never charges you to apply."),
    ("How many credits should I take each semester?",
     "Most bachelor's degrees take about 120 credits. At 15 a semester that's 8 semesters, or 4 years. Usually 12 credits is the minimum to count as full-time. Use the credit hour calculator above, then confirm with your advisor, because your degree plan has the final word."),
    ("Do I have to fill out the FAFSA every year?",
     "Yes. Federal aid is awarded one school year at a time, so you file a new FAFSA for each year you want aid. Many states and colleges set their own deadlines, so earlier is better."),
    ("Will my credits transfer if I change schools?",
     "It depends on both schools, the course and your grade. Check with the new school's registrar before you enroll, and use Transferology to see how courses usually map. Dr. Fedor covers three common reasons in her video, 3 Reasons Your Credits Didn't Transfer."),
    ("Can I change my major and still graduate on time?",
     "Often, yes, especially if you switch early and your general education courses count toward both. Run a what-if degree audit and meet your advisor before you decide."),
    ("I'm a parent. Why can't I see my student's grades?",
     "Under FERPA, once a student is in college the rights to their education records belong to them. Your student can sign a FERPA release with the registrar, or give you proxy access if the school offers it."),
    ("I'm struggling and it's more than school. Where do I go?",
     "If you're in crisis, call or text 988 any time, or text HOME to 741741. On campus, your counseling center is usually free for enrolled students, and your dean of students office can help with emergencies, including food and housing."),
    ("How can I ask Dr. Fedor a question?",
     "Leave it in the comments of any video on the College Conversations channel. The questions students ask are what the channel exists to answer."),
]
