# Increment Planning Process Overview and Gap Analysis

This document provides a comprehensive description of the Increment Planning process, incorporating all provided details, along with an analysis of potential gaps.

### Updated Increment Planning Process Description

The Increment Planning process is a structured, one-day event designed to align all teams (Squads and Chapters) on a committed plan for the upcoming quarter. This single-day format is made possible by a significant amount of pre-planning carried out by the squads and chapters, which streamlines the on-the-day activities.

**Pre-Planning Phase:**
*   In Sprints 17.4 and 17.5, Squads and Chapters meet to discuss the epics planned for Increment 18. These meetings are led by Product Owners and Iteration Managers.
*   Two dedicated dependency meetings are held during these sprints (one in 17.4 and one in 17.5) for teams to raise and discuss dependencies with other squads and chapters.
*   The time between these dependency meetings is used for detailed discussions with relevant stakeholders to clarify dependencies and their timings.
*   Teams engage in preliminary discussions to identify and define dependencies on other teams. These dependencies are negotiated, resulting in a status of **Accepted**, **Blocked**, or **Rejected**.
*   Teams break down their delivery epics into stories and estimate them to understand the estimated size of each epic.
*   Epics are prioritized by Product Owners and the SLT, providing teams with an overall priority focus.
*   With the help of Iteration Managers, teams and Chapters determine their capacity using capacity planning spreadsheets and historical velocity from previous increments. Individual team member availability is factored into these spreadsheets for sprint-to-sprint and overall 6-sprint increment estimation.
*   The facilitator (Agile Coach/Iteration Manager) prepares logistics, tools (Jira, Confluence), and the agenda.

**Planning Day Execution:**
1.  **Opening (09:00):** The day begins with a presentation of the **Strategic Priorities** for the increment, setting the high-level goals. This is followed by a talk from the Executive General Manager on the state of the business and how the Digital and Technology group can support it.
2.  **Team Breakouts (Throughout the day):** The majority of the day is dedicated to team-level planning. Delivery Squads and Chapters work in separate breakout sessions to plan their work for the quarter directly in Jira, utilizing their pre-determined capacity and prioritized epics. This involves defining epics, associated stories, start/end sprints, and T-shirt sizes.
3.  **Risk Management (11:00 & 14:00):** There are two dedicated sessions for the **Risk/Blockers - SLT Discussion**. Teams raise risks to the Senior Leadership Team (SLT) using a **ROAM board**. Iteration Managers and Product Owners from Chapters and Squads attend to discuss the risks and agree on a path forward (Resolved, Owned, Accepted, or Mitigated). The outcomes from this session are fed back to the teams.
4.  **Plan Reviews (13:00 & 15:30):**
    *   A **Draft Plan Review** is held specifically for the Chapters to review their plans. This is a critical step as Chapters' work is often heavily dependent on the plans of other teams, and this review provides an early opportunity to identify and resolve cross-team dependencies.
    *   The day culminates in **Final Plan Playbacks**, where all Squads and Chapters present their finalized Jira plans to the SLT and other stakeholders for final questions and commitment. These plans include epics with start/end sprints and T-shirt sizes.
5.  **Closing (16:30):** The event concludes with a retrospective to gather feedback and identify improvements for the next planning cycle.

**Post-Planning Phase:**
*   The facilitator synthesizes retro action items, follows up on them, and ensures all plans are finalized and accessible in Jira and Confluence.
*   Dependency lifecycle management continues: Dependencies raised are captured in Jira, detailing requirements and the sprint by which they are needed. Once a dependency has been accepted, it is moved into the backlog of the team responsible for delivery and subsequently planned into their sprint work as needed.

### Integrating Operational/Support Work

For teams like Level 1 Support Desk and Networking Infrastructure, who provide essential operational and support services, it is crucial to integrate their work into the Increment Planning process to ensure visibility and proper capacity allocation.

1.  **Create "Operational Epics":** These teams should create specific Epics in Jira for recurring operational or support work (e.g., "IP18 Event Support" or "BAU - Program Support"). This makes the work visible and allows for high-level tracking.
2.  **Define Tasks as Stories:** Break down the operational work into specific, estimable stories under the relevant Operational Epic (e.g., "Source and Deliver Monitors for IP18," "Set up Wi-Fi/Network Infrastructure for IP18," "Conduct Sound Checks for IP18"). These stories should be estimated like any other delivery story.
3.  **Allocate Capacity:** During capacity planning for the increment, these teams must explicitly account for the estimated effort of these operational stories. This means their available capacity for other delivery-focused epics will be reduced accordingly, ensuring that operational commitments are factored into their overall workload.
4.  **Track as Dependencies:** The Iteration Manager for the overall event should formally raise these operational stories as dependencies with the respective support teams during the pre-planning dependency meetings. This ensures the work is tracked, committed to, and has clear ownership and timelines.

### Revised Potential Gaps in the Process

With the added information about capacity planning, here are the remaining potential gaps or areas that might require further definition:

1.  **Cross-Team Dependency Visualization:** While dependencies are identified and managed, there is still no explicit mention of a specific tool or ceremony *during* the planning day to visualize these dependencies across all teams (e.g., a **Program Board** or dependency matrix). This could make it challenging to identify critical paths, potential bottlenecks, or misalignments in timing between multiple dependent teams in real-time during the planning day.
2.  **Feedback Loop from SLT to Teams:** The SLT conducts two risk/blocker discussions. The process for communicating the outcomes of these discussions (e.g., a risk being "Owned" or "Accepted") back to the teams who are in their breakout sessions is not defined. A delay or lack of clarity in this feedback could lead to teams planning based on outdated or incorrect assumptions.
3.  **Draft Plan Review for Squads:** The agenda explicitly mentions a "Draft Plan Review" for Chapters, but not for Delivery Squads. If Squads only present their plans for the first time at the *final* playback, there is a higher risk of discovering significant issues or misalignments too late in the day to effectively address them without impacting the overall schedule.
4.  **Alignment with Strategic Priorities (Mechanism):** While the day starts with strategic priorities and epics are prioritized by Product Owners and SLT, the explicit *mechanism* for teams to ensure their planned work directly traces back to these strategic priorities during the breakout sessions is not fully detailed. Is there a specific template, checklist, or review step to ensure this alignment?
5.  **Definition of "Committed Plan" Detail:** The outcome is a "committed plan defined in Jira (including epic and their associated stories)." While stories are estimated in the lead-up, the level of detail required for all associated stories to be considered "committed" by the end of the day is not entirely clear. Does "committed" mean all stories are fully detailed and estimated, or is a higher-level understanding sufficient for the commitment?
