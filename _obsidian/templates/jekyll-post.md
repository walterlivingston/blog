<%*
const title = await tp.system.prompt("Post Title");
const slug = title.toLowerCase()
  .replace(/[^a-z0-9\s-]/g, "")
  .replace(/\s+/g, "-")
  .replace(/-+/g, "-");

const date = tp.date.now("YYYY-MM-DD");
const datetime = tp.date.now("YYYY-MM-DD HH:mm:ss");
const filename = `${date}-${slug}`;

await tp.file.rename(filename);

tR = `---
layout: post
title: "${title}"
date: ${datetime}
categories: [personal]
tags: []
comments: true
---
`
%>
