# Karl Shultz
**Senior QA Engineer**  
Wake Forest, North Carolina | karl.shultz@gmail.com | [LinkedIn](https://www.linkedin.com/in/karl-shultz-9386949/) | [GitHub](https://github.com/krshultz)

## Summary

Seasoned QA engineer with deep experience across enterprise endpoint security, CI/CD infrastructure, and storage systems. If you're looking for a QA Engineer who finds things other people miss, I am that QA Engineer. I get there with an exploratory approach, by tracing defects to their root cause in the source code, and by using AI to extend my judgment rather than replace it.

I know when to reach for clever automation and when manual testing is the better tool, and I now ship code in an agentic workflow where AI agents plan, build, and test changes, with me as the human check.

## Skills

**Languages:** Python, Java, Groovy, Bash, PowerShell, SQL (PostgreSQL, SQLite)

**Test Tools:** pytest, Playwright MCP, TestCafe, Postman, Bruno, Jira XRay

**CI/CD and Infrastructure:** Jenkins (Pipeline), Docker, AWS EC2, VMware, Grafana, Git and GitHub, Bitbucket, Jira, Linear

**AI and Agentic Workflows:** Claude Code (custom skills, subagents, MCP servers), agentic development and testing pipelines, human-in-the-loop review of AI output

**Methodologies:** Manual, automated, API, UI/browser, regression, smoke, and usability testing; Agile

## Career Highlights

- **Prolific defect finder:** Opened over 250 bugs and improvements in just over a year on Tanium Enforce, and was later consistently the highest bug-opener on Tanium Comply by a significant margin
- **Park (Claude Code skill):** Captures side findings mid-test, then walks them through structured triage; read-only AI subagents verify each finding against the source code at a pinned commit
- **Socratest (Claude Code skill):** Quizzes the tester on how a change could fail before testing begins
- **QA leadership:** Managed 8 direct reports across about 6 product teams; helped grow Tanium's North American QA team to 25 engineers and launch its Krakow, Poland QA team

## Experience

### Atomic Empire *(August 2026 – Present)*

**Senior QA Engineer**

E-commerce platform for collectible card games, comics, and gaming merchandise (ASP.NET MVC, AWS), where AI agents plan, implement, review, and test each change, with human approval at every gate.

- Serve as the human-in-the-loop quality gate for AI-written code: test each change on the test server, post evidence-backed results, and decide whether it advances to merge or returns for revisions
- Extended the team's AI browser-testing agent with pre-run checks, data-safety rules, structured reporting, and a Playwright MCP mode for third-party payment windows
- Found high-impact defects in payment, gift card, checkout, and order workflows through exploratory testing; traced root causes through the C# source and documented them with commit-pinned evidence
- Authored the QA roadmap (test data optimization, unit, API, and end-to-end testing, CI quality gates, process) after assessing existing test coverage

### Tanium *(July 2020 – June 2026)*

**Senior Quality Assurance Engineer | March 2024 – June 2026**

Returned to an individual contributor role after a company-wide restructuring eliminated the QA Manager layer.

- One of four Senior QA Engineers on Tanium Comply, an enterprise compliance and vulnerability scanning product (Joval, CIS-CAT, and SCC scan engines), testing the web UI and endpoint client code
- Led the test effort for a major codebase rewrite; found a high volume of UI, filtering, and data migration defects
- Tested Remote Authenticated Scanning (SSH and WinRM to Unix, Linux, and Windows endpoints); found credential handling and remote authentication defects
- Found more defects with AI-assisted testing than any other team member
- Built Claude AI skills for upgrade monitoring, Jira XRay test suggestions, and scan diagnostics, checking AI output for rule drift and unverified conclusions
- Wrote automated API tests in Python with pytest for uploading and validating scan engines; used Grafana dashboards to diagnose issues and inform Go/No-Go decisions

**QA Engineering Manager | November 2021 – March 2024**

Managed 8 direct reports across about 6 product teams, providing technical direction and career development.

- Helped move the organization from ad-hoc releases to a structured semi-annual bundle release process
- Co-authored the job description for Tanium's first Staff QA Engineer role

**Senior Quality Assurance Engineer | July 2020 – November 2021**

Built QA procedures from scratch for Tanium Enforce (Windows registry, BitLocker, and AppLocker policy).

- Developed a TestCafe browser-based smoke test suite running at build time
- Built tooling to automate Jira state transitions from pull request activity
- Co-authored a formal release process with go/no-go requirements; wrote multiple test plans

### CloudBees

**Senior Software Engineer | August 2016 – July 2020**

Open source Jenkins, focused on the Pipeline suite and GitHub/Bitbucket plugins; owned quality processes for initiatives including Declarative Pipelines.

- Contributed bug fixes with automated tests to Jenkins plugins including GitHub Branch Source
- Built Groovy Jenkins Pipeline jobs testing multiple plugins, triggered by pull requests and merges
- Ran CloudBees Core in a Kubernetes cluster to build and test unreleased plugin code; maintained AWS EC2 test environments
- Extended the Acceptance Test Harness for Blue Ocean with Selenium/Java tests, and contributed to an open source Pipeline performance testing project using Docker

### TOSHIBA Global Commerce Solutions

**Software Engineer and Test Lead | July 2014 – August 2016**

- Directed testing for a five-person QA team across North Carolina and Guadalajara, Mexico
- Maintained Windows and 4690 lab infrastructure (Python, PowerShell, Bash); supported a client rollout on-site

### Earlier Experience

**NetApp** (QA Engineer, SnapMirror Vault QA lead), **GlaxoSmithKline** (Software Tester, FDA-regulated test automation), and **IBM** (Software Engineer, appliance server product lead)

## Education and Patents

- **BA, Psychology:** University of North Carolina at Chapel Hill
- **US Patents 6,898,705 and 6,636,958:** Appliance server re-provisioning and drive partitioning
