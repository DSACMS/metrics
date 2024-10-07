---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2024-10-07
permalink: /DSACMS/

org: DSACMS
reportID: REPORT-2024-10-07
date_stampThisWeek: 2024-10-07
date_stampLastWeek: 2024-10-07
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
        <td>2408</td>
        <td>2403</td>
        <td style="color: #45c527" >5</td>
        <td style="color: #45c527" >0.21%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>153</td>
        <td>153</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>84</td>
        <td>84</td>
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
        <td>27</td>
        <td>26</td>
        <td style="" >1</td>
        <td style="" >3.8%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>379</td>
        <td>379</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>94</td>
        <td>90</td>
        <td style="" >4</td>
        <td style="" >4.3%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>18</td>
        <td>18</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>43</td>
        <td>44</td>
        <td style="color: #d31c08" >-1</td>
        <td style="color: #d31c08" >2.3%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>24</td>
        <td>25</td>
        <td style="color: #d31c08" >-1</td>
        <td style="color: #d31c08" >4.1%</td>
      </tr>
      <tr>
        <th scope="row">Followers</th>
        <td>20</td>
        <td>20</td>
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
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_issue_gauge.svg", title: "Issues & PRs Status Breakdown" %}
    <!-- New Issues over Last 6 Months -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_new_issues_by_day_over_last_six_months.svg", title: "New Issues over Last 6 Months" %}
    <!-- Top Committers Bar Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_top_committers.svg", title: "Top Committers" %}
  </div>
</div>