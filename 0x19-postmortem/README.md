0x19-postmortem

# Web Stack Outage Postmortem: When Nginx Took a Nap

![Nginx Sleeping]
![ad3fc218-708c-4435-af14-1261b31f3c00](https://github.com/NanaOdamme/alx-system_engineering-devops/assets/133671534/92debd93-6604-4f9e-9bcb-5f866805b880)

## Issue Summary:
- **Duration:** Jan 29, 2023, 8:00am - 9:30am
- **Impact:** Nginx server decided to take a siesta, causing service downtime. Approximately 80% of users experienced slow or interrupted service. It's like the Nginx server went on a coffee break without telling anyone!
- **Root Cause:** It turns out, our dear Apache 2 service needed a wakeup call—a restart was all it needed to snap out of its slumber and let Nginx do its thing.

## Timeline:
- **8:00:** Oh no! Monitoring alert wakes us up to Nginx server's beauty sleep.
- **8:05:** Started poking around Nginx configs and logs like a detective looking for clues.
- **8:20:** Thought Nginx had a bit too much coffee, so tried restarting it. No luck!
- **8:30:** Called in the senior devops engineer for backup; turns out, it was Apache 2 hogging the blanket.
- **8:45:** Apache 2 service was snoring—er, failed—so we gave it a gentle nudge with a restart.
- **9:00:** Apache 2 finally decided to wake up, and Nginx stretched its legs back to life.
- **9:30:** Service restored, and everyone breathed a sigh of relief. Back to business!

## Root Cause and Resolution:
- **Root Cause:** Apache 2 decided to take an unexpected nap, causing Nginx to join in the slumber party.
- **Resolution:** A gentle restart of Apache 2 brought it back to reality, and Nginx happily resumed its duties.

## Corrective and Preventative Measures:
- **Improvements/Fixes:**
  - Implement robust monitoring for Apache 2 service health..
  - Establish automated alerts for Apache 2 service failures.
  - Document and maintain clear procedures for handling web server failures.
  - Keep a stash of caffeine handy for emergency situations (just kidding... or maybe not).
- **Tasks:**
  - Patch Apache 2 server to the latest version and ensure it gets its beauty sleep regularly.
  - Set up automatic alerts for any signs of server sleepwalking.
  - Conduct a thorough review of server configurations to ensure they're not sleep-inducing.

## Conclusion:
While the outage might have felt like a bad dream, it served as a reminder to keep our servers well-rested and alert. By implementing the suggested improvements and completing the outlined tasks, we'll ensure our web stack stays awake and responsive, providing uninterrupted service to our users.

*Remember, even servers need their beauty sleep—just not during peak hours!*

