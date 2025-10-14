const Image = require("@11ty/eleventy-img")
const lucideIcons = require("@grimlink/eleventy-plugin-lucide-icons")
const path = require("path")

async function resizeImage(src, sizes, outputFormat = "png") {
  const stats = await Image(src, {
    widths: [+sizes.split("x")[0]],
    formats: [outputFormat],
    outputDir: "frontend/img", //this needs to be updated after testing
  })

  const props = stats[outputFormat].slice(-1)[0]
  return props.url
}

module.exports = function (eleventyConfig) {
  const markdownIt = require("markdown-it")
  const markdownItLinkAttributes = require("markdown-it-link-attributes")

  // Set target="_blank" and rel="noopener noreferrer" on external links
  // Opens in a new tab
  const markdownLib = markdownIt({
    html: true,
  }).use(markdownItLinkAttributes, {
    pattern: /^https?:/,
    attrs: {
      target: "_blank",
      rel: "noopener noreferrer",
    },
  })
  eleventyConfig.setLibrary("md", markdownLib)
  eleventyConfig.addFilter("markdown", (value) => markdownLib.render(value))
  eleventyConfig.addPairedShortcode("mdBlock", (content) =>
    markdownLib.render(content)
  )

  // This allows Eleventy to watch for file changes during local development.
  eleventyConfig.setUseGitIgnore(false)

  eleventyConfig.addLiquidShortcode("resizeImage", resizeImage)
  eleventyConfig.addFilter("resizeImage", resizeImage)

  // Format a URL for concise user display, e.g. https://www.example.gov/foo/
  // becomes example.gov/foo. The returned URL *should* be equivalent, but it
  // might not be for broken sites (and won't be HTTPS in any case); don't use
  // the output of this function as the href, only for user display.
  eleventyConfig.addFilter("prettifyUrl", (url) => {
    url = url.replace(/^https?:\/\//, "")
    url = url.replace(/^www\./, "")
    url = url.replace(/\/$/, "")
    return url
  })

  eleventyConfig.addFilter("findObject", function (array, value) {
    return array.find((item) => item["name"] === value)
  })

  eleventyConfig.addFilter("findProjectsInOrg", function (array, value) {
    return array.filter((item) => item["owner"] === value)
  })

  eleventyConfig.addFilter("fileExists", function (filePath) {
    const fs = require("fs")
    return fs.existsSync(filePath)
  })

  // Create a collection of items without permalinks so that we can reference them
  // in a separate shortcode to pull in partial content directly
  eleventyConfig.addCollection("partials", (collectionApi) =>
    collectionApi.getAll().filter(({ data: { permalink } }) => !permalink)
  )

  eleventyConfig.addPassthroughCopy({
    "frontend/src/img": "assets/img",
    "frontend/src/js": "src/js",
    "frontend/_includes/css": "css",
    "frontend/site/_includes/js": "assets/js",
    "frontend/site/_graphs": "assets/img/graphs",
    "node_modules/@uswds/uswds/dist/img": "assets/img",
    "node_modules/@uswds/uswds/dist/fonts": "fonts",
  })

  eleventyConfig.setLiquidOptions({ outputEscape: "escape" })
  eleventyConfig.addPlugin(lucideIcons, {
    class: "custom-class",
    width: 17,
    height: 17,
    stroke: "currentColor",
    "stroke-width": 2,
  })

  const siteTarget = process.env.SITE_TARGET || "site";

  const inputDir = path.join(__dirname, `frontend/site-${siteTarget}`);
  fallbackDir = path.join(__dirname, "frontend/site");

  const fs = require("fs");
  const finalInput = fs.existsSync(inputDir) ? `frontend/site-${siteTarget}` : `frontend/site`;

  console.log(`Building Eleventy site using input folder: ${finalInput}`);

  const pathPrefix = process.env.ELEVENTY_ENV.includes("production") ? "/metrics" : ""

  return {
    dir: {
      input: finalInput,
      output: `dist-${siteTarget}`,
      includes: "_includes",
      layouts: "_layouts",
    },
    templateFormats: ["html", "md", "liquid", "11ty.js"],
    passthroughFileCopy: true,
    pathPrefix,
  };
};
