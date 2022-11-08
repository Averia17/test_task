-- 1
SELECT notebooks_brand.title,
(SELECT COUNT(*) FROM notebooks_notebook WHERE notebooks_brand.id = notebooks_notebook.brand_id) AS count
FROM notebooks_brand order by count desc;

-- 2
SELECT CEILING((width/5))::numeric(5,0) * 5 as w,
CEILING((depth/5))::numeric(5,0) * 5 as d,
CEILING((height/5))::numeric(5,0) * 5 as h, count(*) FROM notebooks_notebook
group by w, d, h
order by w, d, h;