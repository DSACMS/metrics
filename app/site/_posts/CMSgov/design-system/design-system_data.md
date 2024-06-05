---
layout: repo-report
title: Open Source at CMS Metrics Report for design-system | REPORT-2024-06-05
permalink: /CMSgov/design-system/

org: CMSgov
repo: design-system
reportID: REPORT-2024-06-05
date_stampThisWeek: 2024-06-05
date_stampLastWeek: 2024-06-05
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
        <td>2247</td>
        <td>2242</td>
        <td style="color: #45c527" >5</td>
        <td style="color: #45c527" >0.22%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>239</td>
        <td>238</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.42%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>14</td>
        <td>13</td>
        <td style="" >1</td>
        <td style="" >7.4%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>225</td>
        <td>225</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>12</td>
        <td>7</td>
        <td style="" >5</td>
        <td style="" >53%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>2109</td>
        <td>2100</td>
        <td style="color: #45c527" >9</td>
        <td style="color: #45c527" >0.43%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>639</td>
        <td>639</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>84</td>
        <td>84</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>293</td>
        <td>292</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.34%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>56</td>
        <td>56</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2>Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section"  baseurl: site.baseurl, path: "/CMSgov/design-system/issue_gauge_design-system_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/design-system/commit_sparklines_design-system_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/CMSgov/design-system/firstResponseForClosedPR_design-system_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/design-system/total_line_makeup_design-system_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/CMSgov/design-system/new_commit_contributors_by_day_over_last_month_design-system_data.svg, /CMSgov/design-system/new_commit_contributors_by_day_over_last_six_months_design-system_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
</div>