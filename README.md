# Current — arrears platform prototype

An interactive prototype of a collections and customer-communication platform for
a UK energy supplier, built as a single self-contained HTML file with no build
step and no dependencies beyond two webfonts.

**[Open the prototype →](https://mosesdex.github.io/current-arrears-prototype/)**

It covers three surfaces, switchable from the top rail:

| Surface | What it is |
|---|---|
| **Agent workspace** | Three panes — queue, conversation, account context. Six cases, each demonstrating a different rule the system has to hold to. |
| **Admin console** | Operations, message routing and failover, workflow gates, template linting, roles and access, import validation, contact rules, audit trail. |
| **Customer app** | Seven screens in a device frame: balance, payment, affordability, Direct Debit, circumstances, messages, dispute. |

- **Typing indicators**, in the app only. SMS has no presence field that could
  carry "typing", so the indicator exists on the channel where it is true and the
  interface says so rather than implying otherwise.
- **Presence on a conversation** — who else is reading it, and who is typing a
  reply right now, because two agents answering one person in arrears is the
  failure this prevents.
- **Assignment and handover.** Reassign from the conversation or from the manager
  view. Suggestions are ordered by care training first on a care-flagged case and
  then by who is carrying least, never by who is fastest. A handover moves the
  whole case and **does not reset the customer's waiting time**.
- **Photographs from customers** — a meter reading or a tenancy agreement settles
  in one image what a fortnight of messages cannot. Location metadata is stripped
  on receipt, readings are transcribed by a person, and an attachment that turns
  out to be health information routes to a restricted path.
- **A drafting assistant** that drafts and never sends. It is given only the case
  fields it needs, every suggestion goes through the same linter as a typed
  message, the drafts it rejected are shown rather than hidden, and on a
  care-routed account it declines to write a payment request at all.
- **Manager statistics** — a first-reply distribution rather than an average, who
  is carrying what, what nobody has picked up, and every handover with its reason.

### Six channels, one conversation

Text, app, WhatsApp, email, call and letter are properties of a message, not
separate inboxes — two inboxes for one customer means two versions of what was
said, and the one an ombudsman asks for will be the other one.

- **Calls**, agent-initiated only. There is no predictive or power dialler in
  this design: predictive dialling produces abandoned calls and answer-machine
  detection produces the silent call the rules exist to prevent. A live call bar
  runs mute, hold and end, and the **recording pauses itself when the payment
  step opens** rather than relying on the agent to remember, because card and
  security numbers must never reach a recording.
- **A five-step disclosure protocol on screen during the call**, not in a
  training deck, for the moment a customer tells you something difficult. A call
  where somebody mentions their health becomes special category data
  mid-sentence and routes to a restricted store.
- **Call outcomes are chosen, not inferred.** On the care-flagged case,
  completing the welfare call is the only thing that lifts the suspension on
  arrears activity — no timer and no manager override.
- **Email**, with the subject line treated as a lock-screen preview: a subject
  naming the balance **blocks the send**, on the same minimisation rule as an
  SMS body. No payment links, ever, because a collections email carrying a link
  is indistinguishable from the phishing it invites.
- **Bounces classified three ways** — the customer's circumstances, a dead
  address, or our own defect — the same shape as a Direct Debit return, with a
  hard bounce suppressing the channel rather than entering a retry queue.
- **WhatsApp**, built as additive and never load-bearing. It is the only channel
  here that **reintroduces the dependency this platform exists to remove**: the
  provider in front of it is swappable, but there is no second WhatsApp behind
  it. Outside a 24-hour service window only a template Meta has approved can be
  sent, the approver is Meta rather than us, and quality rating is derived from
  user blocks and reports — which people in arrears do. So nothing in the
  collections process depends on it, and every template that matters also exists
  as a letter.
- **Quick-reply buttons** return a known value instead of a sentence to
  interpret, which takes the guessing out of the question that matters most.
- **Declining a call switches the channel** and is logged as reaching a
  preference, never as a customer who would not engage.

### Working together on a conversation to show or hide the annotation layer that
explains the rule behind each decision. Dark mode follows the operating system
and can be overridden.

## Things in here that are deliberate

- **Arrears, never balance.** The two differ whenever an unbilled charge or an
  unapplied payment is in flight, and chasing a balance chases money that is not
  yet owed.
- **Care state sits above the money**, in every panel that shows both. An agent
  who reads the balance first has already framed the conversation.
- **Care states are violet, never red.** Red is the arrears signal in this
  product, and a person needing help is not a risk to be flagged.
- **The composer can be blocked by policy rather than by permission** — a
  disputed balance, a breathing space moratorium, an unconfirmed identity and a
  bereavement each stop sending for a different reason, and the interface says
  which.
- **No agent ranking.** The team table is deliberately unsorted and unscored.
- **No propensity or likelihood-to-pay scoring anywhere**, and no automated
  decision about a person.
- **A per-recipient frequency governor that fails closed.** Send four messages in
  one conversation and it holds the fourth, because mobile operators cap what a
  handset can receive per hour and discard the overflow silently rather than
  returning an error.

## Synthetic data

Every customer, balance, meter reference, conversation and phone number is
invented. Mobile numbers sit inside `07700 900000`–`900999` and the single
landline inside `029 2018 0xxx`, the ranges the regulator reserves for fiction,
so no fixture can collide with a real subscriber. Nothing here is drawn from a
real customer record.

## Running it

There is nothing to install.

```bash
open index.html
```

Any static host will serve it. The file is self-contained apart from Inter,
Newsreader and JetBrains Mono, which load from Google Fonts.

## Scope

This is a prototype for discussion, not a product. It has no backend, no
authentication and no persistence: state lives in the page and resets on reload.
The research and architecture behind it live in a separate repository.

## Licence

MIT — see [LICENSE](LICENSE).
