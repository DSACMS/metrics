const production = process.env.NODE_ENV === "production"

// const host = production ? "https://dsacms.github.io" : "http://0.0.0.0:8080"
const host = "http://0.0.0.0:8080"

// For modifying the <base> tag
const baseurl = production ? "/metrics" : ""

module.exports = {
  name: "CMS Metrics Website",
  title: "CMS.gov Open Source Repository Metrics",
  description: "Powered by the Open Source Program Office (OSPO) at the Digital Service at the Centers for Medicare and Medicaid Services.",
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
