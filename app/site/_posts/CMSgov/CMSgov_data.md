---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2025-05-25
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2025-05-25
date_stampThisWeek: 2025-05-25
date_stampLastWeek: 2025-05-25
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
        <td>56229</td>
        <td>55722</td>
        <td style="color: #45c527" >507</td>
        <td style="color: #45c527" >0.91%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>1008</td>
        <td>1006</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.2%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>114</td>
        <td>116</td>
        <td style="color: #45c527" >-2</td>
        <td style="color: #45c527" >1.7%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>894</td>
        <td>890</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >0.45%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>216</td>
        <td>227</td>
        <td style="color: #45c527" >-11</td>
        <td style="color: #45c527" >5%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>21405</td>
        <td>21042</td>
        <td style="color: #45c527" >363</td>
        <td style="color: #45c527" >1.7%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4939</td>
        <td>4843</td>
        <td style="" >96</td>
        <td style="" >2%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>612</td>
        <td>605</td>
        <td style="color: #45c527" >7</td>
        <td style="color: #45c527" >1.2%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1544</td>
        <td>1534</td>
        <td style="color: #45c527" >10</td>
        <td style="color: #45c527" >0.65%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1828</td>
        <td>1820</td>
        <td style="color: #45c527" >8</td>
        <td style="color: #45c527" >0.44%</td>
      </tr>
      <tr>
        <th scope="row">Followers</th>
        <td>30</td>
        <td>30</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2 class="graph-section-title">Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMSgov_issue_gauge.svg", title: "Issues & PRs Status Breakdown", modal_description: "This graph provides an overview of the statuses of issues and pull requests in the organization. It categorizes them into open issues, open pull requests, and closed and merged pull requests, helping track progress and worklad distribution." %}
    <!-- New Issues over Last 6 Months -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMSgov_new_issues_by_day_over_last_six_months.svg", title: "New Issues over Last 6 Months", modal_description: "These graphs illustrate the number of new contributors joining the organization over time. They show data for six-month intervals, providing insights into contributor growth and onboarding rates." %}
    <!-- Top Committers Bar Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMSgov_top_committers.svg", title: "Top Committers", modal_description: "This graph highlights the top contributors with the organizations, ranked by the number of commits they have made. It provides insights into the most active members driving developement efforts and their relative contributions to the organization's repositories." %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMSgov_libyear_timeline.svg", title: "Dependency Libyears", modal_description: "This timeline graph visualizes the age of dependencies in the organization in terms of 'libyears.' It highlights how up-to-date the dependencies are and the potential risk of outdated libraries." %}
  </div>
</div>