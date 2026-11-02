const $ = id => document.getElementById(id);
const keys = ['q','manufacturer','type','sort','player','rendered','studio'];
const selected = new Map();
const identity = v => v.variant_id || v.record_id;
let offset = 0, total = 0, controller, timer, renderedVariants = 0;
const pageSize = 36;
const number = (value, suffix='') => value == null ? 'Unavailable' : `${new Intl.NumberFormat(undefined,{maximumFractionDigits:1}).format(value)}${suffix}`;
const speedPair = (mph, kmh) => mph == null || kmh == null ? 'Unavailable' : `${Math.round(mph)} mph / ${Math.round(kmh)} km/h`;
function element(tag,text){const node=document.createElement(tag);if(text!=null)node.textContent=String(text);return node;}
function dl(list, pairs){for(const [key,value] of pairs){list.append(element('dt',key),element('dd',value == null || value === '' ? 'Unavailable' : value));}}
function compare(){
  $('compare-panel').hidden=!selected.size;
  const table=$('comparison');table.replaceChildren();
  const rows=[['Vehicle',v=>`${v.title} · ${v.appearance || v.record_id}`],['Calculated top speed · HUD',v=>speedPair(v.stats.hud_top_speed_mph,v.stats.hud_top_speed_kmh)],['World-space gearing ceiling',v=>speedPair(v.stats.top_speed_mph,v.stats.top_speed_kmh)],['Horsepower',v=>number(v.stats.horsepower,' hp')],['UI mass',v=>number(v.stats.mass_kg,' kg')],['Physics mass',v=>number(v.stats.physics_mass_kg,' kg')],['Drivetrain',v=>v.drivetrain],['Max RPM',v=>number(v.stats.max_rpm)],['Appearance',v=>v.appearance]];
  for(const [label,get] of rows){const row=element('tr');row.append(element('th',label));for(const v of selected.values())row.append(element('td',get(v)||'Unavailable'));table.append(row);}
}
function card(v){
  const node=$('vehicle-card').content.firstElementChild.cloneNode(true);
  const image=node.querySelector('img'),placeholder=node.querySelector('.placeholder');
  image.hidden=!v.image_url;placeholder.hidden=!!v.image_url;if(v.variant_id&&!v.image_url)placeholder.textContent=v.render_status==='failed'?'Variant render needs repair':'Variant render pending';
  if(v.image_url){image.src=v.image_url;image.alt=`${v.title} — ${v.preview_kind==='studio'?'studio render':'game-rendered vehicle preview'}`;image.addEventListener('error',()=>{image.hidden=true;placeholder.hidden=false;});}
  node.querySelector('.image-kind').textContent=v.preview_kind==='studio'?(v.preview_metadata?.geometry==='game_appearance_proxy'?'3D render · game LOD':'Studio render'):v.image_url?(v.preview_metadata?.model_fallback?'Game preview · shared model':'Game preview · record icon'):'';
  const views=node.querySelector('.view-buttons');
  for(const [name,url] of Object.entries(v.image_views||{})){const button=element('button',({hero:'¾ front',front:'Front',back:'Rear',left:'Side',right:'Right',rear:'¾ rear',side:'Side'})[name]||name);button.type='button';button.setAttribute('aria-label',`${v.title}: ${name} view`);button.addEventListener('click',()=>{image.src=url;image.alt=`${v.title} — ${name} render`;views.querySelectorAll('button').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));});button.setAttribute('aria-pressed',String(url===v.image_url));views.append(button);}
  views.hidden=!views.childElementCount;
  if(v.image_url){image.classList.add('expandable');image.tabIndex=0;const expand=()=>{const dialog=$('render-viewer');dialog.querySelector('img').src=image.src;dialog.querySelector('img').alt=image.alt;dialog.querySelector('p').textContent=v.preview_metadata?.note||v.title;dialog.showModal();};image.addEventListener('click',expand);image.addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault();expand();}});}
  node.querySelector('.make').textContent=[v.manufacturer||'Unknown manufacturer',v.vehicle_type,v.year].filter(Boolean).join(' / ');
  node.querySelector('h2').textContent=v.title;
  node.querySelector('.variant').textContent=v.variant_id?v.appearance:v.record_id;
  for(const [label,value] of [['Calculated top speed · HUD',speedPair(v.stats.hud_top_speed_mph,v.stats.hud_top_speed_kmh)],['World-space gearing ceiling',speedPair(v.stats.top_speed_mph,v.stats.top_speed_kmh)],['Horsepower',number(v.stats.horsepower,' hp')],['UI mass',number(v.stats.mass_kg,' kg')],['Drivetrain',v.drivetrain||'Unavailable'],['Max RPM',number(v.stats.max_rpm)]]){const group=element('div');dl(group,[[label,value]]);node.querySelector('.specs').append(group);}
  node.querySelector('.copy-id').addEventListener('click',async event=>{try{await navigator.clipboard.writeText(v.record_id);event.target.textContent='Copied';setTimeout(()=>event.target.textContent='Copy record ID',1200);}catch{$('status').textContent=`Copy this ID: ${v.record_id}`;}});
  const copyVariant=node.querySelector('.copy-variant');copyVariant.hidden=!v.variant_id;copyVariant.addEventListener('click',async()=>{try{await navigator.clipboard.writeText(JSON.stringify({record_id:v.record_id,appearance:v.appearance},null,2));copyVariant.textContent='Copied';setTimeout(()=>copyVariant.textContent='Copy variant',1200);}catch{$('status').textContent=`${v.record_id} / ${v.appearance}`;}});
  const checkbox=node.querySelector('.compare');checkbox.checked=selected.has(identity(v));
  checkbox.addEventListener('change',()=>{if(checkbox.checked){if(selected.size>=4){checkbox.checked=false;$('status').textContent='Compare up to four vehicles at a time.';return;}selected.set(identity(v),v);}else selected.delete(identity(v));compare();});
  node.querySelector('.description').textContent=v.description||'No localized vehicle description in this snapshot.';
  dl(node.querySelector('.source'),[['Record',v.record_id],['Appearance',v.appearance],['App resource',v.appearance_resource],['App definition',v.appearance_definition],['Entity records',(v.compatible_records||[]).join(', ')],['Entity',v.template],['Source',v.source],['Parent',v.parent],['Content',v.expansion],['Tags',v.tags.join(', ')],['Armored',v.armored?'Yes':'No'],['Weapons',v.weapons.join(', ')],['Torque (raw)',number(v.stats.engine_torque)],['Max RPM',number(v.stats.max_rpm)],['Physics mass',number(v.stats.physics_mass_kg,' kg')],['Icon',v.icon_id],['Preview note',v.preview_metadata?.note],['Speed calculation',v.performance?.note],['Speedometer curve',v.performance?.hud_curve_resource],['Torque curve',v.performance?.torque_curve_resource],['Curve at max normalized RPM',JSON.stringify(v.performance?.torque_curve_at_normalized_rpm_1||{})]]);
  const gearTable=element('table'),head=element('tr');for(const name of ['Gear','Limit m/s','HUD mph / km/h'])head.append(element('th',name));gearTable.append(head);
  v.gears.forEach((gear,index)=>{const speed=v.performance?.gears?.[index];const row=element('tr');for(const value of [index===0?'R':index,number(gear.maxSpeed),speedPair(speed?.hud_mph,speed?.hud_kmh)])row.append(element('td',value));gearTable.append(row);});
  node.querySelector('.gears').append(v.gears.length?gearTable:element('p','No gear data.'));
  return node;
}
async function load(){
  controller?.abort();controller=new AbortController();
  const params=new URLSearchParams({limit:String(pageSize),offset:String(offset),variants:'1'});
  for(const key of keys){const input=$(key);const value=input.type==='checkbox'?(input.checked?'1':''):input.value;if(value)params.set(key,value);}
  history.replaceState(null,'',`?${params}`);$('status').textContent='Loading vehicles…';
  try{const response=await fetch(`/api/vehicles?${params}`,{signal:controller.signal});const data=await response.json();if(!response.ok)throw Error(data.error||'Unable to load vehicles');total=data.total;$('vehicles').replaceChildren(...data.vehicles.map(card));$('status').textContent=total?`${offset+1}–${Math.min(offset+pageSize,total)} of ${total.toLocaleString()} appearance variants`:'No vehicles match. Try clearing a filter.';$('page').textContent=`Page ${Math.floor(offset/pageSize)+1} of ${Math.max(1,Math.ceil(total/pageSize))}`;$('previous').disabled=offset===0;$('next').disabled=offset+pageSize>=total;}catch(error){if(error.name!=='AbortError')$('status').textContent=error.message;}
}
async function init(){
  const params=new URLSearchParams(location.search);for(const key of keys){if(!params.has(key))continue;const input=$(key);if(input.type==='checkbox')input.checked=params.get(key)==='1';else if(!['manufacturer','type'].includes(key))input.value=params.get(key);}
  const response=await fetch('/api/summary');if(!response.ok)throw Error('Vehicle catalog is unavailable');const data=await response.json();
  renderedVariants=data.rendered_variants||0;
  $('totals').textContent=`${data.vehicles.toLocaleString()} records / ${(data.appearance_variants||0).toLocaleString()} appearances / ${(data.rendered_variants||0).toLocaleString()} variant renders`;
  for(const [id,values] of [['manufacturer',data.manufacturers],['type',data.types]]){for(const value of values){const option=element('option',value);option.value=value;$(id).append(option);}$(id).value=params.get(id)||'';}
  offset=Math.max(0,Number.parseInt(params.get('offset')||'0',10)||0);await load();
}
$('filters').addEventListener('submit',event=>event.preventDefault());
$('filters').addEventListener('input',()=>{clearTimeout(timer);timer=setTimeout(()=>{offset=0;load();},200);});
$('clear').addEventListener('click',()=>{$('filters').reset();offset=0;load();});
$('previous').addEventListener('click',()=>{offset=Math.max(0,offset-pageSize);load();});$('next').addEventListener('click',()=>{offset+=pageSize;load();});
$('clear-compare').addEventListener('click',()=>{selected.clear();compare();document.querySelectorAll('.compare').forEach(input=>input.checked=false);});
init().catch(error=>$('status').textContent=error.message);
$('close-render').addEventListener('click',()=>$('render-viewer').close());

setInterval(async()=>{if(document.hidden)return;try{const response=await fetch('/api/summary');if(!response.ok)return;const data=await response.json();const count=data.rendered_variants||0;$('totals').textContent=`${data.vehicles.toLocaleString()} records / ${(data.appearance_variants||0).toLocaleString()} appearances / ${count.toLocaleString()} variant renders`;if(count!==renderedVariants){renderedVariants=count;if(!document.querySelector('details[open]')&&!$('render-viewer').open)await load();}}catch{}},15000);
