module.exports = {
  plugins: [
    require("postcss-import"),
    require("autoprefixer"),
    ...(process.env.NODE_ENV.includes("production")
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
