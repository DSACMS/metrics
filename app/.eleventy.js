const Image = require("@11ty/eleventy-img")
const lucideIcons = require("@grimlink/eleventy-plugin-lucide-icons")

async function resizeImage(src, sizes, outputFormat = "png") {
  const stats = await Image(src, {
    widths: [+sizes.split("x")[0]],
    formats: [outputFormat],
    outputDir: "./site/img",
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
    "src/img": "assets/img",
    "src/js": "src/js",
    "site/img": "assets/img",
    "site/_includes/css": "css",
    "site/_includes/js": "assets/js",
    "site/_graphs": "assets/img/graphs",
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

  const pathPrefix = process.env.ELEVENTY_ENV.includes("production") ? "/metrics" : ""

  return {
    dir: {
      input: "site/",
      output: "dist",
      includes: "_includes",
      layouts: "_layouts",
    },
    templateFormats: ["html", "md", "liquid", "11ty.js"],
    passthroughFileCopy: true,
    pathPrefix,
  }
}
