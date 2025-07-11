---
layout: repo-report
title: Open Source at CMS Metrics Report for price-transparency-guide | REPORT-2025-06-15
permalink: /CMSgov/price-transparency-guide/

org: CMSgov
repo: price-transparency-guide
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
        <td>269</td>
        <td>269</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>85</td>
        <td>85</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>16</td>
        <td>16</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>69</td>
        <td>69</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>6</td>
        <td>3</td>
        <td style="" >3</td>
        <td style="" >67%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>104</td>
        <td>103</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.97%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>14</td>
        <td>13</td>
        <td style="" >1</td>
        <td style="" >7.4%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>117</td>
        <td>117</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>396</td>
        <td>393</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >0.76%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>297</td>
        <td>292</td>
        <td style="color: #45c527" >5</td>
        <td style="color: #45c527" >1.7%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-section">
  <br>
  <h2 class="graph-section-title">Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section"  baseurl: site.baseurl, path: "/CMSgov/price-transparency-guide/issue_gauge_price-transparency-guide_data.svg", title: "Issues & PRs Status Breakdown", modal_description: "This graph provides an overview of the statuses of issues and pull requests in the repository. It categorizes them into open issues, open pull requests, and closed and merged pull requests, helping track progress and worklad distribution." %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/price-transparency-guide/commit_sparklines_price-transparency-guide_data.svg", title: "Commits by Month", modal_description: "This line graph represents contributor activity over time by showing the number of commits made each month. It provides insights into trends in developement and periods of high and low activity." %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/CMSgov/price-transparency-guide/firstResponseForClosedPR_price-transparency-guide_data.png", title: "First Response For Closed PR", modal_description: "This scatterplot visualizes the time it takes for the first response on closed pull requests. Each point represents a pull request, helping analyze the response times and potential bottlenecks in the review process." %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/CMSgov/price-transparency-guide/new_commit_contributors_by_day_over_last_month_price-transparency-guide_data.svg, /CMSgov/price-transparency-guide/new_commit_contributors_by_day_over_last_six_months_price-transparency-guide_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval", modal_description: "These graphs illustrate the number of new contributors joining the project over time. They show data for one-month and six-month intervals, providing insights into contributor growth and onboarding rates." %}
  </div>
</div>

<div class="graph-section">
  <br>
  <h2 class="graph-section-title">COCOMO Graphs</h2>
  <div class="all-graphs">
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/price-transparency-guide/total_line_makeup_price-transparency-guide_data.svg", title: "Line Complexity", modal_description: "This graph measures the complexity of the codebase over time by analyzing the number lines, blank line and commented lines." %}
    <!-- Languages Graphs - Summary + Predominant -->
    {% assign optionsArray = 'Summary, Predominant' | split: ',' %}
    {% assign graphsArray = "/CMSgov/price-transparency-guide/language_summary_price-transparency-guide_data.svg, /CMSgov/price-transparency-guide/predominant_langs_price-transparency-guide_data.svg" | split: ',' %}
    {% render "graph-toggle" baseurl: site.baseurl, name:"language-information" options: optionsArray, graphs: graphsArray, title: "Language Information" %}
    <!-- Average Issue Resolution Time -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/price-transparency-guide/average_issue_resolution_time_price-transparency-guide_data.svg", title: "Average Issue Resolution Time", modal_description: "This graph tracks the average time taken to resolve issues in the repository. It helps identify trends in issue resolution efficiency and areas for improvement." %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/price-transparency-guide/libyear_timeline_price-transparency-guide_data.svg", title: "Dependency Libyears", modal_description: "This timeline graph visualizes the age of dependencies in the repository in terms of 'libyears.' It highlights how up-to-date the dependencies are and the potential risk of outdated libraries." %}
    <!-- DRYness Percentages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/price-transparency-guide/DRYness_price-transparency-guide_data.svg", title: "DRYness Percentage Graph", modal_description: "This graph measures the 'Don't Repeat Yourself' (DRY) principle compliance in the repository. It calculates the percentage of duplicate versus unique code, indicating the overall efficiency of the codebase." %}
    <!-- Cost Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/price-transparency-guide/estimated_project_costs_price-transparency-guide_data.svg", title: "Estimated Costs", modal_description: "This graph provides an estimation of the developement cost and corresponding value of the project." %}
     <!-- Time Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/price-transparency-guide/estimated_project_time_price-transparency-guide_data.svg", title: "Estimated Time", modal_description: "This graph estimates the time required to develop the project." %}
    <!-- Contributor Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/price-transparency-guide/estimated_people_contributing_price-transparency-guide_data.svg", title: "Estimated Individual Contributors", modal_description: "This graph visualizes the number of contributors required to complete a project, based on current scope." %}
  </div>
</div>