import"./chunk-b3cdbad1.js";import{G as a,a as c}from"./chunk-94b083a2.js";import{S as s}from"./chunk-ceedaaa2.js";const t=new s;chrome.tabs.query({active:!0,currentWindow:!0,url:"*://*.bing.com/maps*"},(async s=>{t.afterSetupCallbacks.push((async()=>{if(t.S.openFlag=!0,await a.sleep(200),s.length<=0)e();else try{await c("SHOW-OR-HIDE-IFRAME",{display:"block"})}catch(r){e()}}))}));const e=()=>{chrome.tabs.create({url:"https://bing.com/maps"})};
