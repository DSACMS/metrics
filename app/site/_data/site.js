const isProduction = process.env.NODE_ENV.includes("production")
const isTest = process.env.NODE_ENV.includes("test")

const host = (isProduction && !isTest) ? "https://dsacms.github.io" : "http://localhost:8080"

// For modifying the <base> tag
const baseurl = isProduction ? "/metrics" : ""

module.exports = {
  name: "CMS Metrics Website",
  title: "CMS.gov Open Source Repository Metrics",
  description: "Powered by the Open Source Program Office (OSPO) at the Digital Service at the Centers for Medicare and Medicaid Services.",
  type: "website",
  baseurl,
  url: `${host}${baseurl}`,
  domain: (host || "").replace("https://", ""),
  production: isProduction,
  robots: isProduction,
  locale: "en-US",
  // TODO: Add nav elements for deployment
  nav: [{ url: "/about/", label: "About" }],
}
