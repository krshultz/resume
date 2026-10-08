# Karl Shultz
**Senior QA Engineer**  
Wake Forest, North Carolina | karl.shultz@gmail.com | [LinkedIn](https://www.linkedin.com/in/karl-shultz-9386949/) | [GitHub](https://github.com/krshultz)

## Summary

Senior QA Engineer with 25+ years of experience across enterprise endpoint security, CI/CD infrastructure, and storage systems. If you're looking for a QA Engineer who finds things other people miss, I am that QA Engineer.

I believe that clever automation and well-thought-out manual testing are both important, and I know when to use each. More recently, I've built a practice of AI-assisted testing with custom Claude skills, and I've found more bugs because of it.

## Skills

**Languages:** Python, Java, Groovy, Bash, PowerShell, Perl, SQL (PostgreSQL, SQLite)

**Test Tools:** pytest, Selenium, TestCafe, JUnit, Postman, Bruno, Jira XRay

**CI/CD and Infrastructure:** Jenkins (Pipeline), Docker, AWS EC2, VMware, Hyper-V, Grafana, Git and GitHub, Jira

**AI-Assisted Testing:** Claude, including custom skill development

**Methodologies:** Manual, automated, API, UI/browser, regression, smoke, and usability testing; Agile

## Experience

### Tanium *(July 2020 – June 2026)*

**Senior Quality Assurance Engineer | March 2024 – June 2026**

Returned to an individual contributor role following a company-wide restructuring that eliminated the QA Manager layer.

- One of four Senior QA Engineers on Tanium Comply, an enterprise compliance and vulnerability scanning product (CIS benchmarks; Joval, CIS-CAT, and SCC scan engines), testing both the web UI and client code on managed endpoints
- Led the test effort for a major codebase rewrite; identified and documented a high volume of UI, filtering, and data migration defects
- Tested Remote Authenticated Scanning, validating SSH key/password and WinRM connections to Unix, Linux, and Windows endpoints; found defects in credential handling and remote authentication workflows
- Consistently the highest bug-opener on the team by a significant margin, including more AI-assisted defects than any other team member; received two consecutive years of glowing peer feedback
- Designed and built a suite of Claude AI skills to augment manual and exploratory testing, checking AI output for rule drift and unverified conclusions before acting on it:
    - **Upgrade Monitor:** Tracked upgrades via SSH across devices, normalizing logs into before/after comparisons
    - **Test Ride-Along:** Suggested test approaches from Jira XRay cases and the underlying source changes
    - **Assessment Timeline:** Instrumented scans end-to-end, diagnosing failures across scan types and engines
- Wrote automated API tests in Python with pytest for uploading and validating scan engines; used Grafana dashboards to diagnose issues and inform Go/No-Go decisions

**QA Engineering Manager | November 2021 – March 2024**

Managed 8 direct reports across about 6 product teams, providing technical direction and career development.

- Helped move the organization from ad-hoc, team-by-team releases to a structured semi-annual bundle release process
- Co-authored the job description for Tanium's first Staff QA Engineer role
- Determined QA staffing across product teams; helped grow the North American QA team to 25 engineers and launch the Krakow, Poland QA team

**Senior Quality Assurance Engineer | July 2020 – November 2021**

Built QA procedures from scratch for Tanium Enforce, validating Windows policy enforcement including registry, BitLocker, and AppLocker settings.

- Developed a TestCafe browser-based smoke test suite running at build time
- Built tooling to automate Jira state transitions from pull request activity, and improved build pipeline speed and flexibility
- Co-authored a formal release process with go/no-go requirements; wrote multiple test plans
- Opened over 250 bugs and improvements in just over a year

### CloudBees

**Senior Software Engineer | August 2016 – July 2020**

Open source Jenkins, focused on the Pipeline suite and GitHub/Bitbucket plugins; owned quality processes for initiatives including Declarative Pipelines.

- Contributed bug fixes with automated tests to Jenkins plugins including GitHub Branch Source
- Built Jenkins Pipeline jobs in Groovy providing automated test coverage across multiple plugins, triggered by pull requests and merges
- Ran CloudBees Core in a Kubernetes cluster to build and test unreleased plugin code, and maintained AWS EC2 test environments using AMIs for cloning
- Extended the Acceptance Test Harness for Blue Ocean with Selenium/Java tests, and contributed to an open source Pipeline performance testing project using Docker

### TOSHIBA Global Commerce Solutions

**Software Engineer and Test Lead | July 2014 – August 2016**

- Directed testing for a five-person QA team across North Carolina and Guadalajara, Mexico
- Maintained lab infrastructure integrating Windows and 4690 systems using Python, PowerShell, and Bash; supported an on-site retail client rollout

### NetApp

**QA Engineer | August 2010 – July 2014**

- Led QA for SnapMirror Vault (ONTAP 8.2.0); QA Release Lead for SAN components of ONTAP 8.2.1
- Co-authored SnapMirror automation in Perl; prototyped Selenium/Java tests for OnCommand

### GlaxoSmithKline (GSK)

**Software Tester | April 2010 – August 2010**

- Automated tests (Java, Selenium RC, JUnit) for an R&D web app in an FDA-regulated environment

### IBM

**Software Engineer | January 2000 – June 2008**

- Product lead for a caching proxy appliance server; designed performance and scalability testing for IBM Director 5.1; led Linux driver installation work for System x servers

## Education and Patents

- **BA, Psychology:** University of North Carolina at Chapel Hill
- **US Patents 6,898,705 and 6,636,958:** Appliance server re-provisioning and drive partitioning
