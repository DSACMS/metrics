const fs = require("fs");
const path = require("path");

module.exports = function () {
  const dataDirectory = path.join(__dirname);
  const projects = [];

  // Read the list of organization directories
  const orgDirectories = fs.readdirSync(dataDirectory);

  // Iterate through organization directories
  orgDirectories.forEach((orgDirectory) => {
    // Construct the full path to the organization directory
    const orgDirectoryPath = path.join(dataDirectory, orgDirectory);

    // Check if the path is a directory
    if (fs.statSync(orgDirectoryPath).isDirectory()) {
      // Read the list of project directories within the organization directory
      const projectDirectories = fs.readdirSync(orgDirectoryPath);

      // Iterate through project directories
      projectDirectories.forEach((projectDirectory) => {
        const dataFileName = projectDirectory + "_data.json";
        const projectDataFilePath = path.join(
          orgDirectoryPath,
          projectDirectory,
          dataFileName
        );

        // Find and add $project-name_data.json file in each project directory
        if (fs.existsSync(projectDataFilePath)) {
          const projectData = JSON.parse(
            fs.readFileSync(projectDataFilePath, "utf8")
          );

          projects.push(projectData);
        }
      });
    }
    
  });
  
  return projects
};
