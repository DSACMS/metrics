module.exports = {
  plugins: [
    require("postcss-import"),
    require("autoprefixer"),
    ...(process.env.NODE_ENV === "production"
      ? [
          require("cssnano"),
          require("@fullhuman/postcss-purgecss")({
            content: [
              "./site/**/*.liquid",
              "./site/**/*.html",
              "./site/**/*.md",
              "./src/**/*.js",
            ],
            safelist: ["usa-js-loading"],
            extractors: [
              {
                extractor: require("purgecss-from-html"),
                extensions: ["html"],
              },
            ],
          }),
        ]
      : []),
  ],
}