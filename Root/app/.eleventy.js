const fs = require("fs")
const path = require("path")
const Image = require("@11ty/eleventy-img")
const EleventyVitePlugin = require("@11ty/eleventy-plugin-vite")
const { EleventyHtmlBasePlugin } = require("@11ty/eleventy")

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

  eleventyConfig.addShortcode(
    "image",
    async function (src, alt, sizes = "100vw") {
      const metadata = await Image(src, {
        widths: [600, 800],
        formats: ["webp", "jpeg"],
        outputDir: "./site/img",
      })
      const lowsrc = metadata.jpeg[0]
      const highsrc = metadata.jpeg[metadata.jpeg.length - 1]
      return `<picture>
      ${Object.values(metadata)
        .map((imageFormat) => {
          return `  <source type="${
            imageFormat[0].sourceType
          }" srcset="${imageFormat
            .map((entry) => entry.srcset)
            .join(", ")}" sizes="${sizes}">`
        })
        .join("\n")}
				<img
					src="${lowsrc.url}"
					width="${highsrc.width}"
					height="${highsrc.height}"
					alt="${alt}"
					loading="lazy"
					decoding="async">
    </picture>`
    }
  )
  eleventyConfig.addNunjucksAsyncShortcode("resizeImage", resizeImage)
  eleventyConfig.addLiquidShortcode("resizeImage", resizeImage)
  eleventyConfig.addFilter("resizeImage", resizeImage)

  // Used to avoid nunjucks escaping includes of imported CSS
  // cssnano was converting media queries with ID values to "{#"
  // Can also be used for nunjucks-style import within 11ty.js files
  eleventyConfig.addShortcode("includefile", function (filename) {
    return fs.readFileSync(
      path.join(__dirname, "site", "_includes", filename),
      "utf8"
    )
  })

  // format a URL for concise user display, e.g. https://www.example.gov/foo/
  // becomes example.gov/foo. The returned URL *should* be equivalent, but it
  // might not be for broken sites (and won't be HTTPS in any case); don't use
  // the output of this function as the href, only for user display.
  eleventyConfig.addFilter("prettifyUrl", (url) => {
    url = url.replace(/^https?:\/\//, "")
    url = url.replace(/^www\./, "")
    url = url.replace(/\/$/, "")
    return url
  })

  // Create a collection of items without permalinks so that we can reference them
  // in a separate shortcode to pull in partial content directly
  eleventyConfig.addCollection("partials", (collectionApi) =>
    collectionApi.getAll().filter(({ data: { permalink } }) => !permalink)
  )

  eleventyConfig.addPassthroughCopy({
    "src/img": "assets/img",
    "site/img": "assets/img",
    "src/js": "assets/js",
    "node_modules/@uswds/uswds/dist/img": "assets/img",
  })

  eleventyConfig.setLiquidOptions({ outputEscape: "escape" })

  const pathPrefix = process.env.NODE_ENV == "production" ? "/open" : "/"

  eleventyConfig.addPlugin(EleventyVitePlugin, {
    viteOptions: { base: pathPrefix },
  })

  return {
    dir: {
      input: "site/",
      output: "dist",
      includes: "_includes",
      layouts: "_layouts",
    },
    templateFormats: ["html", "md", "liquid", "11ty.js"],
    htmlTemplateEngine: "njk",
    passthroughFileCopy: true,
    pathPrefix,
  }
}
