---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2025-02-23
permalink: /DSACMS/

org: DSACMS
reportID: REPORT-2025-02-23
date_stampThisWeek: 2025-02-23
date_stampLastWeek: 2025-02-23
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
        <td>4683</td>
        <td>4658</td>
        <td style="color: #45c527" >25</td>
        <td style="color: #45c527" >0.54%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>216</td>
        <td>212</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >1.9%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>119</td>
        <td>115</td>
        <td style="" >4</td>
        <td style="" >3.4%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>97</td>
        <td>97</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>69</td>
        <td>64</td>
        <td style="" >5</td>
        <td style="" >7.5%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>1026</td>
        <td>1018</td>
        <td style="color: #45c527" >8</td>
        <td style="color: #45c527" >0.78%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>227</td>
        <td>224</td>
        <td style="" >3</td>
        <td style="" >1.3%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>25</td>
        <td>25</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>77</td>
        <td>76</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >1.3%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>35</td>
        <td>35</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Followers</th>
        <td>27</td>
        <td>26</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >3.8%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2 class="graph-section-title">Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_issue_gauge.svg", title: "Issues & PRs Status Breakdown", modal_description: "This graph provides an overview of the statuses of issues and pull requests in the organization. It categorizes them into open issues, open pull requests, and closed and merged pull requests, helping track progress and worklad distribution." %}
    <!-- New Issues over Last 6 Months -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_new_issues_by_day_over_last_six_months.svg", title: "New Issues over Last 6 Months", modal_description: "These graphs illustrate the number of new contributors joining the organization over time. They show data for six-month intervals, providing insights into contributor growth and onboarding rates." %}
    <!-- Top Committers Bar Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_top_committers.svg", title: "Top Committers", modal_description: "This graph highlights the top contributors with the organizations, ranked by the number of commits they have made. It provides insights into the most active members driving developement efforts and their relative contributions to the organization's repositories." %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_libyear_timeline.svg", title: "Dependency Libyears", modal_description: "This timeline graph visualizes the age of dependencies in the organization in terms of 'libyears.' It highlights how up-to-date the dependencies are and the potential risk of outdated libraries." %}
  </div>
</div>