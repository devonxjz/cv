"use client";

import Image from "next/image";
import { useRef, type ReactNode } from "react";
import { motion, useReducedMotion } from "motion/react";
import { useGSAP } from "@gsap/react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { GraduationCap, Trophy, UsersThree } from "@phosphor-icons/react";

gsap.registerPlugin(ScrollTrigger, useGSAP);

export function Reveal({
  children,
  className = "",
  delay = 0,
}: {
  children: ReactNode;
  className?: string;
  delay?: number;
}) {
  const reduce = useReducedMotion();

  return (
    <motion.div
      className={className}
      initial={reduce ? false : { opacity: 0, y: 28 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.2 }}
      transition={{ duration: 0.7, delay, ease: [0.16, 1, 0.3, 1] }}
    >
      {children}
    </motion.div>
  );
}

export function ImageReveal({
  children,
  className = "",
  delay = 0,
}: {
  children: ReactNode;
  className?: string;
  delay?: number;
}) {
  const reduce = useReducedMotion();

  return (
    <motion.div
      className={className}
      initial={reduce ? false : { opacity: 0, scale: 0.84 }}
      whileInView={{ opacity: 1, scale: 1 }}
      viewport={{ once: true, amount: 0.25 }}
      transition={{ duration: 0.85, delay, ease: [0.16, 1, 0.3, 1] }}
    >
      {children}
    </motion.div>
  );
}

type JourneyItem = {
  period: string;
  title: string;
  text: string;
  icon: "education" | "award" | "community";
  images?: Array<{
    src: string;
    alt: string;
    fit: "contain" | "cover";
  }>;
};

const journeyIcons = {
  education: GraduationCap,
  award: Trophy,
  community: UsersThree,
};

export function JourneyStack({ items }: { items: JourneyItem[] }) {
  const scope = useRef<HTMLDivElement>(null);
  const reduce = useReducedMotion();

  useGSAP(
    () => {
      if (reduce || !scope.current || window.matchMedia("(max-width: 767px)").matches) return;

      const cards = gsap.utils.toArray<HTMLElement>(".journey-card");
      cards.forEach((card, index) => {
        if (index === cards.length - 1) return;

        ScrollTrigger.create({
          trigger: card,
          start: "top top",
          endTrigger: cards[cards.length - 1],
          end: "top top",
          pin: true,
          pinSpacing: false,
        });

        gsap.to(card, {
          scale: 0.92,
          opacity: 0.42,
          ease: "none",
          scrollTrigger: {
            trigger: cards[index + 1],
            start: "top bottom",
            end: "top top",
            scrub: true,
          },
        });
      });
    },
    { scope, dependencies: [reduce] },
  );

  return (
    <div ref={scope} className="journey-stack">
      {items.map((item) => {
        const Icon = journeyIcons[item.icon];
        return (
        <article
          className={`journey-card${item.images ? " journey-card-with-media" : ""}`}
          key={item.title}
        >
          <div className="journey-card-inner content-wrap">
            <span className="journey-period">{item.period}</span>
            <Icon size={56} weight="duotone" aria-hidden="true" />
            <div className="journey-copy">
              <h3>{item.title}</h3>
              <p>{item.text}</p>
            </div>
            {item.images && (
              <div className="journey-media" aria-label={`${item.title} images`}>
                {item.images.map((media) => (
                  <a
                    className={`journey-media-frame journey-media-${media.fit}`}
                    href={media.src}
                    key={media.src}
                    target="_blank"
                    rel="noreferrer"
                    aria-label={`Open full image: ${media.alt}`}
                  >
                    <Image
                      src={media.src}
                      alt={media.alt}
                      fill
                      sizes="(max-width: 767px) calc(100vw - 2rem), (max-width: 1050px) 46vw, 19vw"
                    />
                  </a>
                ))}
              </div>
            )}
          </div>
        </article>
        );
      })}
    </div>
  );
}
