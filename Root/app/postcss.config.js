module.exports = {
    plugins: [
      require("autoprefixer"),
      ...(process.env.NODE_ENV === "production"
        ? [
            require("@fullhuman/postcss-purgecss")({
              content: ["./.11ty-vite/**/*.html", "./.11ty-vite/**/*.js"],
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