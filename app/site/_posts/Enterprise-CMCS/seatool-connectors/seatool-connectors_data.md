---
layout: repo-report
title: Open Source at CMS Metrics Report for seatool-connectors | REPORT-2025-06-15
permalink: /Enterprise-CMCS/seatool-connectors/

org: Enterprise-CMCS
repo: seatool-connectors
reportID: REPORT-2025-06-15
date_stampThisWeek: 2025-06-15
date_stampLastWeek: 2025-06-15
---
<div class="summary-table">
  <table class="usa-table usa-table--borderless">
    <h2> Summary Table </h2>
    <thead>
      <tr>
        <th scope="col">Metric</th>
        <th scope="col">Latest</th>
        <th scope="col">Previous</th>
        <th scope="col">Diff</th>
        <th scope="col">% Diff</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Commits</th>
        <td>209</td>
        <td>207</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.96%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>31</td>
        <td>31</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>0</td>
        <td>0</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>31</td>
        <td>31</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>10</td>
        <td>11</td>
        <td style="color: #45c527" >-1</td>
        <td style="color: #45c527" >9.5%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>91</td>
        <td>87</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >4.5%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>30</td>
        <td>30</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>0</td>
        <td>0</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>0</td>
        <td>0</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>6</td>
        <td>6</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-section">
  <br>
  <h2 class="graph-section-title">Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section"  baseurl: site.baseurl, path: "/Enterprise-CMCS/seatool-connectors/issue_gauge_seatool-connectors_data.svg", title: "Issues & PRs Status Breakdown", modal_description: "This graph provides an overview of the statuses of issues and pull requests in the repository. It categorizes them into open issues, open pull requests, and closed and merged pull requests, helping track progress and worklad distribution." %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/seatool-connectors/commit_sparklines_seatool-connectors_data.svg", title: "Commits by Month", modal_description: "This line graph represents contributor activity over time by showing the number of commits made each month. It provides insights into trends in developement and periods of high and low activity." %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/Enterprise-CMCS/seatool-connectors/firstResponseForClosedPR_seatool-connectors_data.png", title: "First Response For Closed PR", modal_description: "This scatterplot visualizes the time it takes for the first response on closed pull requests. Each point represents a pull request, helping analyze the response times and potential bottlenecks in the review process." %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/Enterprise-CMCS/seatool-connectors/new_commit_contributors_by_day_over_last_month_seatool-connectors_data.svg, /Enterprise-CMCS/seatool-connectors/new_commit_contributors_by_day_over_last_six_months_seatool-connectors_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval", modal_description: "These graphs illustrate the number of new contributors joining the project over time. They show data for one-month and six-month intervals, providing insights into contributor growth and onboarding rates." %}
  </div>
</div>

<div class="graph-section">
  <br>
  <h2 class="graph-section-title">COCOMO Graphs</h2>
  <div class="all-graphs">
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/seatool-connectors/total_line_makeup_seatool-connectors_data.svg", title: "Line Complexity", modal_description: "This graph measures the complexity of the codebase over time by analyzing the number lines, blank line and commented lines." %}
    <!-- Languages Graphs - Summary + Predominant -->
    {% assign optionsArray = 'Summary, Predominant' | split: ',' %}
    {% assign graphsArray = "/Enterprise-CMCS/seatool-connectors/language_summary_seatool-connectors_data.svg, /Enterprise-CMCS/seatool-connectors/predominant_langs_seatool-connectors_data.svg" | split: ',' %}
    {% render "graph-toggle" baseurl: site.baseurl, name:"language-information" options: optionsArray, graphs: graphsArray, title: "Language Information" %}
    <!-- Average Issue Resolution Time -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/seatool-connectors/average_issue_resolution_time_seatool-connectors_data.svg", title: "Average Issue Resolution Time", modal_description: "This graph tracks the average time taken to resolve issues in the repository. It helps identify trends in issue resolution efficiency and areas for improvement." %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/seatool-connectors/libyear_timeline_seatool-connectors_data.svg", title: "Dependency Libyears", modal_description: "This timeline graph visualizes the age of dependencies in the repository in terms of 'libyears.' It highlights how up-to-date the dependencies are and the potential risk of outdated libraries." %}
    <!-- DRYness Percentages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/seatool-connectors/DRYness_seatool-connectors_data.svg", title: "DRYness Percentage Graph", modal_description: "This graph measures the 'Don't Repeat Yourself' (DRY) principle compliance in the repository. It calculates the percentage of duplicate versus unique code, indicating the overall efficiency of the codebase." %}
    <!-- Cost Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/seatool-connectors/estimated_project_costs_seatool-connectors_data.svg", title: "Estimated Costs", modal_description: "This graph provides an estimation of the developement cost and corresponding value of the project." %}
     <!-- Time Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/seatool-connectors/estimated_project_time_seatool-connectors_data.svg", title: "Estimated Time", modal_description: "This graph estimates the time required to develop the project." %}
    <!-- Contributor Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/seatool-connectors/estimated_people_contributing_seatool-connectors_data.svg", title: "Estimated Individual Contributors", modal_description: "This graph visualizes the number of contributors required to complete a project, based on current scope." %}
  </div>
</div>