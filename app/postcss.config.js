module.exports = {
  plugins: [
    require("postcss-import"),
    require("autoprefixer"),
    ...(process.env.ELEVENTY_ENV.includes("production")
      ? [
          require("cssnano"),
          require("@fullhuman/postcss-purgecss")({
            content: [
              "./site/**/*.liquid",
              "./site/**/*.html",
              "./site/**/*.md",
              "./src/**/*.js",
            ],
          }),
        ]
      : []),
  ],
}
