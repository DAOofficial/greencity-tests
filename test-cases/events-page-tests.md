# Test cases for Greencity events page

## Test case 1
**Title:** Filter events by status

**Test Case ID:** GC-EV-01

**Summary:** Check if the user can filter events using status tags.

**Priority:** Medium

**Preconditions:**
1. URL is open: `https://www.greencity.cx.ua/#/greenCity/events`.
2. At least one event with "Open" and one with "Closed" tag exists.

**Test Steps:**

| Step | Action | Data | Expected Result |
| :--- | :--- | :--- | :--- |
| 1 | Select the "Status" filter button. | N/A | A dropdown menu appears containing checkboxes: "Any status", "Open", "Closed". |
| 2 | Click on the "Open" checkbox in the list. | Status: "Open" | Only open events are displayed. |
| 3 | Deselect the "Open" checkbox. | N/A | All events are displayed. |
| 4 | Click on the "Closed" checkbox in the list. | Status: "Closed" | Only closed events are displayed. |
| 5 | Deselect the "Closed" checkbox, select "Any status". | N/A | All events are displayed, all checkboxes are selected. |
| 6 | Deselect the "Any status" checkbox. | N/A | All events are displayed. |
| 7 | Select both "Closed" and "Open". | Status: "Open", "Closed" | All events are displayed, all checkboxes are selected. |

---

## Test case 2

**Title:** Search events by title

**Test Case ID:** GC-EV-02

**Summary:** Check if the user can search events by their title.

**Priority:** Low

**Preconditions:**
1. URL is open: `https://www.greencity.cx.ua/#/greenCity/events`.
2. At least one event with the "Event" title exists, no events containing "Event54321" exist.

**Test Steps:**

| Step | Action | Data | Expected Result |
| :--- | :--- | :--- | :--- |
| 1 | Type the title into search field. | "Event" | Events containing "Event" in the title are displayed. |
| 2 | Clear the search field. | N/A | All events are displayed. |
| 3 | Type the title into search field. | "Event54321" | "We didn't find any results matching to this search" is displayed. |

---

## Test Case 3

**Title:** Verify only registered user can create event

**Test Case ID:** GC-EV-03

**Summary:** Check that the user is prompted to log in when creating an event.

**Priority:** High

**Preconditions:**
1. URL is open: `https://www.greencity.cx.ua/#/greenCity/events`.
2. User is not authorized.

**Test Steps:**

| Step | Action | Data | Expected Result |
| :--- | :--- | :--- | :--- |
| 1 | Click the "Create event" button. | N/A | Sign in modal window is displayed. |
| 2 | Click on the "Close" button (X). | N/A | Sign in modal window is closed. |