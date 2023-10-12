const production = process.env.NODE_ENV === "production"

const host = production ? process.env.SITE_HOST : "http://0.0.0.0:8080"

// For modifying the <base> tag
const baseurl = production ? "" : ""

module.exports = {
  name: "CMS Open Source Repo Metrics",
  title: "CMS Open Source Repo Metrics",
  description: "Website containing reports and visualizations on repositories in CMSgov github organization.",
  type: "website",
  baseurl,
  url: `${host}${baseurl}`,
  domain: (host || "").replace("https://", ""),
  production,
  robots: production,
  locale: "en-US",
}