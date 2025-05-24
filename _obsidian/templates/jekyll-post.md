<%*
const title = await tp.system.prompt("Post Title");
const slug = title.toLowerCase()
  .replace(/[^a-z0-9\s-]/g, "")         // remove special characters
  .replace(/\s+/g, "-")                 // spaces to hyphens
  .replace(/-+/g, "-");                 // collapse multiple dashes

const date = tp.date.now("YYYY-MM-DD");
const datetime = tp.date.now("YYYY-MM-DD HH:mm:ss");
const filename = `${date}-${slug}`;

await tp.file.rename(filename); // ✅ Auto-renames the note

tR = `---
layout: post
title: "${title}"
date: ${datetime}
categories: [personal]
tags: []
---
`
%>
