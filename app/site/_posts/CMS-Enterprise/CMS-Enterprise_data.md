---
layout: org-report
title: Open Source at CMS Metrics Report for CMS-Enterprise | REPORT-2024-08-04
permalink: /CMS-Enterprise/

org: CMS-Enterprise
reportID: REPORT-2024-08-04
date_stampThisWeek: 2024-08-04
date_stampLastWeek: 2024-08-04
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
        <td>1149</td>
        <td>1141</td>
        <td style="color: #45c527" >8</td>
        <td style="color: #45c527" >0.7%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>4</td>
        <td>4</td>
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
        <td>4</td>
        <td>4</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>47</td>
        <td>49</td>
        <td style="color: #45c527" >-2</td>
        <td style="color: #45c527" >4.2%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>443</td>
        <td>437</td>
        <td style="color: #45c527" >6</td>
        <td style="color: #45c527" >1.4%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>55</td>
        <td>55</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>9</td>
        <td>9</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>5</td>
        <td>5</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>236</td>
        <td>235</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.42%</td>
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
  <h2>Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/CMS-Enterprise_issue_gauge.svg", title: "Issues & PRs Status Breakdown" %}
    <!-- New Issues over Last 6 Months -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/CMS-Enterprise_new_issues_by_day_over_last_six_months.svg", title: "New Issues over Last 6 Months" %}
    <!-- Top Committers Bar Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/CMS-Enterprise_top_committers.svg", title: "Top Committers" %}
  </div>
</div>