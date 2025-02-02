---
layout: repo-report
title: Open Source at CMS Metrics Report for madie-models | REPORT-2025-02-02
permalink: /measureauthoringtool/madie-models/

org: measureauthoringtool
repo: madie-models
reportID: REPORT-2025-02-02
date_stampThisWeek: 2025-02-02
date_stampLastWeek: 2025-02-02
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
        <td>554</td>
        <td>550</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >0.72%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>0</td>
        <td>0</td>
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
        <td>0</td>
        <td>0</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>1</td>
        <td>0</td>
        <td style="" >1</td>
        <td style="" >200%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>218</td>
        <td>216</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.92%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>27</td>
        <td>27</td>
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
        <td>4</td>
        <td>4</td>
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
    {% render "graph-section"  baseurl: site.baseurl, path: "/measureauthoringtool/madie-models/issue_gauge_madie-models_data.svg", title: "Issues & PRs Status Breakdown", modal_description: "This graph provides an overview of the statuses of issues and pull requests in the repository. It categorizes them into open issues, open pull requests, and closed and merged pull requests, helping track progress and worklad distribution." %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/madie-models/commit_sparklines_madie-models_data.svg", title: "Commits by Month", modal_description: "This line graph represents contributor activity over time by showing the number of commits made each month. It provides insights into trends in developement and periods of high and low activity." %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/measureauthoringtool/madie-models/firstResponseForClosedPR_madie-models_data.png", title: "First Response For Closed PR", modal_description: "This scatterplot visualizes the time it takes for the first response on closed pull requests. Each point represents a pull request, helping analyze the response times and potential bottlenecks in the review process." %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/measureauthoringtool/madie-models/new_commit_contributors_by_day_over_last_month_madie-models_data.svg, /measureauthoringtool/madie-models/new_commit_contributors_by_day_over_last_six_months_madie-models_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval", modal_description: "These graphs illustrate the number of new contributors joining the project over time. They show data for one-month and six-month intervals, providing insights into contributor growth and onboarding rates." %}
  </div>
</div>

<div class="graph-section">
  <br>
  <h2 class="graph-section-title">COCOMO Graphs</h2>
  <div class="all-graphs">
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/madie-models/total_line_makeup_madie-models_data.svg", title: "Line Complexity", modal_description: "This graph measures the complexity of the codebase over time by analyzing the number lines, blank line and commented lines." %}
    <!-- Languages Graphs - Summary + Predominant -->
    {% assign optionsArray = 'Summary, Predominant' | split: ',' %}
    {% assign graphsArray = "/measureauthoringtool/madie-models/language_summary_madie-models_data.svg, /measureauthoringtool/madie-models/predominant_langs_madie-models_data.svg" | split: ',' %}
    {% render "graph-toggle" baseurl: site.baseurl, name:"language-information" options: optionsArray, graphs: graphsArray, title: "Language Information" %}
    <!-- Average Issue Resolution Time -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/madie-models/average_issue_resolution_time_madie-models_data.svg", title: "Average Issue Resolution Time", modal_description: "This graph tracks the average time taken to resolve issues in the repository. It helps identify trends in issue resolution efficiency and areas for improvement." %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/madie-models/libyear_timeline_madie-models_data.svg", title: "Dependency Libyears", modal_description: "This timeline graph visualizes the age of dependencies in the repository in terms of 'libyears.' It highlights how up-to-date the dependencies are and the potential risk of outdated libraries." %}
    <!-- DRYness Percentages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/madie-models/DRYness_madie-models_data.svg", title: "DRYness Percentage Graph", modal_description: "This graph measures the 'Don't Repeat Yourself' (DRY) principle compliance in the repository. It calculates the percentage of duplicate versus unique code, indicating the overall efficiency of the codebase." %}
    <!-- Cost Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/madie-models/estimated_project_costs_madie-models_data.svg", title: "Estimated Costs", modal_description: "This graph provides an estimation of the developement cost and corresponding value of the project." %}
     <!-- Time Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/madie-models/estimated_project_time_madie-models_data.svg", title: "Estimated Time", modal_description: "This graph estimates the time required to develop the project." %}
    <!-- Contributor Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/madie-models/estimated_people_contributing_madie-models_data.svg", title: "Estimated Individual Contributors", modal_description: "This graph visualizes the number of contributors required to complete a project, based on current scope." %}
  </div>
</div>