import type { Metadata } from "next";
import { Outfit, Roboto_Mono } from "next/font/google";
import "./globals.css";

const outfit = Outfit({
  variable: "--font-outfit",
  subsets: ["latin", "latin-ext"],
  display: "swap",
});

const robotoMono = Roboto_Mono({
  variable: "--font-roboto-mono",
  subsets: ["latin", "latin-ext"],
  display: "swap",
});

export const metadata: Metadata = {
  metadataBase: new URL("https://devonxjz.vercel.app"),
  title: "Trần Lê Thái | Backend, AI & Security Engineer",
  description:
    "Portfolio of Trần Lê Thái, a backend and AI engineer building reliable, security-aware systems and agentic workflows.",
  openGraph: {
    title: "Trần Lê Thái | Backend × AI × Security",
    description: "Reliable backends, controlled agents and security-aware execution.",
    type: "website",
    images: [{ url: "/og.png", width: 1672, height: 941, alt: "Trần Lê Thái portfolio" }],
  },
  twitter: {
    card: "summary_large_image",
    title: "Trần Lê Thái | Backend × AI × Security",
    description: "Reliable backends, controlled agents and security-aware execution.",
    images: ["/og.png"],
  },
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" className={`${outfit.variable} ${robotoMono.variable}`}>
      <body>{children}</body>
    </html>
  );
}
