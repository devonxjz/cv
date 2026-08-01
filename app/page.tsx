import Image from "next/image";
import {
  ArrowUpRight,
  Brain,
  Code,
  Database,
  DownloadSimple,
  EnvelopeSimple,
  Fingerprint,
  GithubLogo,
  LinkedinLogo,
  MapPin,
} from "@phosphor-icons/react/ssr";
import { ImageReveal, JourneyStack, Reveal } from "./motion-components";

const profile = {
  github: "https://github.com/devonxjz",
  linkedin: "https://www.linkedin.com/in/devonxjz",
  email: "tranlethai11102006@gmail.com",
  resume: "/tran-le-thai-cv.pdf",
};

const capabilities = [
  {
    icon: Code,
    title: "Backend foundations",
    body: "REST APIs, service-layer architecture, containerized workflows and maintainable server-side systems.",
    detail: "Java / Spring / NestJS / Node.js",
    className: "capability capability-wide",
  },
  {
    icon: Brain,
    title: "Agentic AI",
    body: "Tool orchestration, memory, guardrails and observable multi-step workflows.",
    detail: "LLM integration / evaluation",
    className: "capability capability-compact capability-accent",
  },
  {
    icon: Fingerprint,
    title: "Secure by design",
    body: "Permission boundaries, input validation and safe execution built into the system model.",
    detail: "Burp Suite / security labs",
    className: "capability capability-compact capability-pattern",
  },
  {
    icon: Database,
    title: "Data systems",
    body: "Relational and document data models selected around product behavior, not trends.",
    detail: "PostgreSQL / MongoDB / MySQL",
    className: "capability capability-wide capability-dark",
  },
];

const projects = [
  {
    title: "PhongVu AI Sales Agent",
    kind: "Agentic commerce",
    image: "/projects/phongvu-sales-agent.webp",
    imageAlt: "PhongVu commerce banner used by the PhongVu AI Sales Agent",
    imageClassName: "project-image-contain",
    href: "https://github.com/l3vu0ng/PhongVu-AI-Sales-Agent",
  },
  {
    title: "CV-Agent",
    kind: "AI application",
    image: "/projects/cv-agent.png",
    imageAlt: "CV-Agent repository preview",
    imageClassName: "",
    href: "https://github.com/devonxjz/CV-Agent",
  },
  {
    title: "MissLost",
    kind: "Campus platform",
    image: "/projects/misslost.png",
    imageAlt: "MissLost repository preview",
    imageClassName: "",
    href: "https://github.com/devonxjz/MissLost",
  },
  {
    title: "VibeTDU",
    kind: "Interactive learning",
    image: "/projects/vibetdu-live.png",
    imageAlt: "VibeTDU interactive virtual chemistry laboratory",
    imageClassName: "",
    href: "https://github.com/devonxjz/VibeTDU",
  },
  {
    title: "WeatherForecast AI",
    kind: "ML system",
    image: "/projects/weather-ai.png",
    imageAlt: "WeatherForecast AI repository preview",
    imageClassName: "",
    href: "https://github.com/devonxjz/WeatherForecast_ai",
  },
];

const journey = [
  {
    period: "2021-2024",
    title: "Hung Vuong High School for the Gifted",
    text: "Specialized in Informatics, building the algorithmic base behind my engineering work.",
    icon: "education" as const,
  },
  {
    period: "2023",
    title: "Third Prize in School Science and Engineering",
    text: "Recognized at the school-level science and engineering competition.",
    icon: "award" as const,
  },
  {
    period: "2024-Present",
    title: "HCMUTE, Information Technology",
    text: "Studying backend engineering and information security in Ho Chi Minh City.",
    icon: "education" as const,
  },
  {
    period: "2026",
    title: "Agentic AI Build Week 2026",
    text: "Participated in GenAI Fund's Agentic AI Build Week in Ho Chi Minh City, collaborating on practical AI agent development.",
    icon: "community" as const,
    images: [
      {
        src: "/aabw/participation-certificate.png",
        alt: "Certificate of participation awarded to Thai Tran Le for Agentic AI Build Week 2026",
        fit: "contain" as const,
      },
      {
        src: "/aabw/team-photo.jpg",
        alt: "Team photo from Agentic AI Build Week 2026 in Ho Chi Minh City",
        fit: "cover" as const,
      },
    ],
  },
];

const technologies = [
  "Java",
  "Spring",
  "TypeScript",
  "NestJS",
  "Python",
  "PostgreSQL",
  "MongoDB",
  "Docker",
  "Agentic AI",
  "Application Security",
];

function ContactLinks({ footer = false }: { footer?: boolean }) {
  return (
    <div className={footer ? "footer-links" : "hero-actions"}>
      <a className="button button-primary" href={profile.resume} download>
        <DownloadSimple size={19} weight="bold" />
        Download CV
      </a>
      <a
        className="button button-secondary"
        href={profile.github}
        target="_blank"
        rel="noreferrer"
      >
        <GithubLogo size={19} weight="bold" />
        GitHub
      </a>
      {footer && (
        <a
          className="icon-link"
          href={profile.linkedin}
          target="_blank"
          rel="noreferrer"
          aria-label="Find Trần Lê Thái on LinkedIn"
        >
          <LinkedinLogo size={22} weight="bold" />
        </a>
      )}
    </div>
  );
}

export default function Home() {
  return (
    <main id="main-content" className="site-shell">
      <a className="skip-link" href="#profile">Skip to profile</a>

      <nav className="navigation" aria-label="Primary navigation">
        <a className="monogram" href="#profile" aria-label="Trần Lê Thái home">
          TLT<span>.</span>
        </a>
        <div className="nav-links">
          <a href="#work">Work</a>
          <a href="#journey">Journey</a>
          <a href="#contact">Contact</a>
        </div>
        <a className="nav-resume" href={profile.resume} download>
          CV <DownloadSimple size={17} weight="bold" />
        </a>
      </nav>

      <header id="profile" className="hero">
        <div className="hero-grid" aria-hidden="true" />
        <Reveal className="hero-copy">
          <p className="hero-kicker">Backend Engineer / AI Engineer / Security-minded</p>
          <h1>
            I build the systems behind <span>useful AI.</span>
          </h1>
          <p className="hero-summary">
            Reliable backends, controlled agents and security-aware execution for products people can trust.
          </p>
          <ContactLinks />
        </Reveal>

        <ImageReveal className="portrait-stage">
          <div className="portrait-frame">
            <Image
              src="/profile.jpg"
              alt="Illustrated avatar of Trần Lê Thái"
              fill
              sizes="(max-width: 768px) 72vw, 25rem"
              priority
            />
          </div>
        </ImageReveal>
      </header>

      <section className="profile-statement content-wrap">
        <Reveal>
          <p>
            I approach software from two sides: how it works and how it can fail. That means clear service boundaries, observable AI workflows, careful data decisions and execution paths that remain under control.
          </p>
        </Reveal>
      </section>

      <section className="capabilities-section content-wrap" aria-labelledby="capabilities-title">
        <Reveal className="section-heading">
          <h2 id="capabilities-title">What I bring to the build</h2>
        </Reveal>
        <div className="capability-grid">
          {capabilities.map(({ icon: Icon, ...item }, index) => (
            <Reveal key={item.title} className={item.className} delay={index * 0.06}>
              <Icon size={34} weight="duotone" />
              <div>
                <h3>{item.title}</h3>
                <p>{item.body}</p>
              </div>
              <span>{item.detail}</span>
            </Reveal>
          ))}
        </div>
      </section>

      <section className="technology-band" aria-label="Technology stack">
        <div className="marquee-track">
          {[...technologies, ...technologies].map((technology, index) => (
            <span key={`${technology}-${index}`}>{technology}</span>
          ))}
        </div>
      </section>

      <section id="work" className="work-section content-wrap" aria-labelledby="work-title">
        <Reveal className="section-heading work-heading">
          <h2 id="work-title">Projects that connect the layers</h2>
          <p>AI features grounded in real product flows, data models and backend decisions.</p>
        </Reveal>
        <div className="project-grid">
          {projects.map((project, index) => (
            <article className="project-card" key={project.title}>
              <a
                href={project.href}
                target="_blank"
                rel="noreferrer"
                aria-label={`Open ${project.title} repository on GitHub`}
              >
                <ImageReveal className="project-card-image" delay={index * 0.04}>
                  <Image
                    src={project.image}
                    alt={project.imageAlt}
                    className={project.imageClassName}
                    fill
                    loading="eager"
                    sizes="(max-width: 767px) 100vw, 50vw"
                  />
                </ImageReveal>
                <div className="project-card-caption">
                  <span className="project-badge">{project.title}</span>
                  <span className="project-repository">
                    {project.kind}
                    <ArrowUpRight size={16} weight="bold" />
                  </span>
                </div>
              </a>
            </article>
          ))}
        </div>
      </section>

      <section id="journey" className="journey-section" aria-labelledby="journey-title">
        <div className="content-wrap">
          <Reveal className="journey-intro">
            <h2 id="journey-title">Curiosity, tested in public</h2>
            <p>From informatics and science competitions to building AI agents across ASEAN.</p>
          </Reveal>
        </div>
        <JourneyStack items={journey} />
      </section>

      <section className="direction-section content-wrap">
        <Reveal className="direction-copy">
          <h2>Looking for hard, useful problems.</h2>
          <p>
            I am seeking backend, AI engineering, agentic AI or application security opportunities where careful engineering matters.
          </p>
        </Reveal>
        <Reveal className="direction-aside" delay={0.12}>
          <span>Currently studying</span>
          <strong>Information Technology at HCMUTE</strong>
          <span>Focused on</span>
          <strong>Backend engineering and information security</strong>
        </Reveal>
      </section>

      <footer id="contact" className="footer">
        <div className="footer-mark" aria-hidden="true">TLT</div>
        <div className="footer-content content-wrap">
          <Reveal>
            <h2>Let&apos;s build something reliable.</h2>
            <p>Open to internships, collaborative projects and early-career engineering roles.</p>
          </Reveal>
          <div className="footer-bottom">
            <ContactLinks footer />
            <div className="footer-meta">
              {profile.email ? (
                <a href={`mailto:${profile.email}`}>
                  <EnvelopeSimple size={18} weight="bold" /> {profile.email}
                </a>
              ) : (
                <span><EnvelopeSimple size={18} weight="bold" /> Email available on request</span>
              )}
              <span><MapPin size={18} weight="bold" /> Ho Chi Minh City, Vietnam</span>
              <span>© 2026 Trần Lê Thái</span>
            </div>
          </div>
        </div>
      </footer>
    </main>
  );
}
