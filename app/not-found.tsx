import Link from "next/link";

export default function NotFound() {
  return (
    <main className="not-found">
      <p>404</p>
      <h1>This route is not part of the build.</h1>
      <Link className="button button-primary" href="/">Return home</Link>
    </main>
  );
}
