---
layout: repo-report
title: Open Source at CMS Metrics Report for madie-fhir-elm-translator | REPORT-2024-11-24
permalink: /measureauthoringtool/madie-fhir-elm-translator/

org: measureauthoringtool
repo: madie-fhir-elm-translator
reportID: REPORT-2024-11-24
date_stampThisWeek: 2024-11-24
date_stampLastWeek: 2024-11-24
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
        <td>562</td>
        <td>560</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.36%</td>
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
        <td>2</td>
        <td>2</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>25</td>
        <td>24</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >4.1%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>2</td>
        <td>2</td>
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
        <td>0</td>
        <td>0</td>
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
    {% render "graph-section"  baseurl: site.baseurl, path: "/measureauthoringtool/madie-fhir-elm-translator/issue_gauge_madie-fhir-elm-translator_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/madie-fhir-elm-translator/commit_sparklines_madie-fhir-elm-translator_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/measureauthoringtool/madie-fhir-elm-translator/firstResponseForClosedPR_madie-fhir-elm-translator_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/madie-fhir-elm-translator/total_line_makeup_madie-fhir-elm-translator_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/measureauthoringtool/madie-fhir-elm-translator/new_commit_contributors_by_day_over_last_month_madie-fhir-elm-translator_data.svg, /measureauthoringtool/madie-fhir-elm-translator/new_commit_contributors_by_day_over_last_six_months_madie-fhir-elm-translator_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
    <!-- Languages Graphs - Summary + Predominant -->
    {% assign optionsArray = 'Summary, Predominant' | split: ',' %}
    {% assign graphsArray = "/measureauthoringtool/madie-fhir-elm-translator/language_summary_madie-fhir-elm-translator_data.svg, /measureauthoringtool/madie-fhir-elm-translator/predominant_langs_madie-fhir-elm-translator_data.svg" | split: ',' %}
    {% render "graph-toggle" baseurl: site.baseurl, name:"language-information" options: optionsArray, graphs: graphsArray, title: "Language Information" %}
    <!-- Average Issue Resolution Time -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/madie-fhir-elm-translator/average_issue_resolution_time_madie-fhir-elm-translator_data.svg", title: "Average Issue Resolution Time" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/madie-fhir-elm-translator/libyear_timeline_madie-fhir-elm-translator_data.svg", title: "Dependency Libyears" %}
    <!-- DRYness Percentages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/madie-fhir-elm-translator/DRYness_madie-fhir-elm-translator_data.svg", title: "DRYness Percentage Graph" %}
    <!-- Cost Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/madie-fhir-elm-translator/estimated_project_costs_madie-fhir-elm-translator_data.svg", title: "Estimated Costs" %}
     <!-- Time Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/madie-fhir-elm-translator/estimated_project_time_madie-fhir-elm-translator_data.svg", title: "Estimated Time" %}
    <!-- Contributor Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/madie-fhir-elm-translator/estimated_people_contributing_madie-fhir-elm-translator_data.svg", title: "Estimated Individual Contributors" %}
</div>