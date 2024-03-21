const production = process.env.NODE_ENV === "production"

const host = production ? "https://dsacms.github.io" : "http://0.0.0.0:8080"

// For modifying the <base> tag
const baseurl = production ? "/metrics" : ""

module.exports = {
  name: "CMS OSPO Repo Metrics",
  title: "CMS OSPO Repo Metrics",
  description: "Open Source Repository Metrics across CMS.gov",
  type: "website",
  baseurl,
  url: `${host}${baseurl}`,
  domain: (host || "").replace("https://", ""),
  production,
  robots: production,
  locale: "en-US",
  // TODO: Add nav elements for deployment
  nav: [{ url: "/about/", label: "About" }],
}
