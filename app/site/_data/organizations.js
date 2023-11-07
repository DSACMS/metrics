const fs = require("fs");
const path = require("path");

module.exports = function () {
  const dataDirectory = path.join(__dirname);
  var organizations = [];

  // Read the list of organization directories
  var orgDirectories = fs.readdirSync(dataDirectory);

  // Iterate through organization directories
  orgDirectories.forEach((orgDirectory) => {
    // Construct the full path to the organization directory
    const orgDirectoryPath = path.join(dataDirectory, orgDirectory);

    // Check if the path is a directory
    if (fs.statSync(orgDirectoryPath).isDirectory()) {
      const dataFileName = orgDirectory + "_data.json";
        const orgDataFilePath = path.join(
          orgDirectoryPath,
          dataFileName
        );

        // Find and add $project-name_data.json file in the organization directory
        if (fs.existsSync(orgDataFilePath)) {
          const orgData = JSON.parse(
            fs.readFileSync(orgDataFilePath, "utf8")
          );

          organizations.push(orgData);
        }
    }
  });

  return organizations;
};