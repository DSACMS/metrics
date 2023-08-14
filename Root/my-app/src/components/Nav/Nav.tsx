import { Link, useMatch, useResolvedPath } from "react-router-dom";
import React, {ReactNode} from "react";
export default function Navbar() {
  return (
    <nav className="nav">
      <Link to="/" className="site-title">
        CMS Open Source
      </Link>
      <ul>
        <CustomLink to="/">Home</CustomLink>
        <CustomLink to="/Weekly">Weekly Metrics</CustomLink>
        <CustomLink to="/Monthly">Monthly Metrics</CustomLink>
      </ul>
    </nav>
  )
}
interface CustomLinkProps {
    to: string;
    children: React.ReactNode;
}

function CustomLink({ to, children, ...props }: CustomLinkProps) {
  const resolvedPath = useResolvedPath(to)
  const isActive = useMatch({ path: resolvedPath.pathname, end: true });

  return (
    <li className={isActive ? "active" : ""}>
      <Link to={to} {...props}>
        {children}
      </Link>
    </li>
  );
}