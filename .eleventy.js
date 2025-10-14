const path = require("path");
const fs = require("fs");

const frontendConfigPath = "./frontend/.eleventy.js";
let frontendConfig = null;
try {
    frontendConfig = require(frontendConfigPath);
} catch (e) {
    console.warn("Could not load frontend/.eleventy.js");
}

module.exports = function (eleventyConfig) {
    if (typeof frontendConfig === "function") {
        frontendConfig(eleventyConfig);
    }

    const SITE_TARGET = process.env.SITE_TARGET || "external";
    const inputDir = SITE_TARGET === "internal" ? "site-internal" : "site-external";
    const outputDir = SITE_TARGET === "internal" ? "dist-internal" : "dist-external";

    console.log(`Building site: ${SITE_TARGET} (input: ${inputDir}), output: ${outputDir}`);

    return {
        dir: {
            input: inputDir,
            includes: "../frontend/_includes",
            layouts: "../frontend/_layouts",
            data: "_data",
            output: outputDir
        },
        templateFormats: ["html", "md", "liquid", "11ty.js"],
        passthroughFileCopy: true
    };
};