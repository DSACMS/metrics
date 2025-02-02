---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2025-02-02
permalink: /CMSgov/

org: CMSgov
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
        <td>54924</td>
        <td>54858</td>
        <td style="color: #45c527" >66</td>
        <td style="color: #45c527" >0.12%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>999</td>
        <td>995</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >0.4%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>116</td>
        <td>112</td>
        <td style="" >4</td>
        <td style="" >3.5%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>883</td>
        <td>883</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>213</td>
        <td>203</td>
        <td style="" >10</td>
        <td style="" >4.8%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>20364</td>
        <td>20315</td>
        <td style="color: #45c527" >49</td>
        <td style="color: #45c527" >0.24%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4640</td>
        <td>4613</td>
        <td style="" >27</td>
        <td style="" >0.58%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>592</td>
        <td>590</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.34%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1479</td>
        <td>1477</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.14%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1889</td>
        <td>1888</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.053%</td>
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