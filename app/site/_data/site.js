const production = process.env.NODE_ENV === "production"

const host = production ? process.env.SITE_HOST : "http://0.0.0.0:8080"

// For modifying the <base> tag
const baseurl = production ? "/metrics" : ""

module.exports = {
  name: "Open Source at CMS",
  title: "Open Source at CMS",
  description: "DSAC Open Source Website",
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