from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.get('/items/')
async def get_items(q: Optional[str] = Query(..., max_length = 50, min_length = 3)):
  results = {'items' : [{'item_id' : 'Foo'}, {'item_id' : 'Bar'}]}
  if q:
    results.update({'q' : q})
  return results

# '...' - ellipsis : indicates that some value is required
# We can use basic q: str or q: Optional[str] = None 
# Or we could do q: str = Query(None,*params*) for more custom validation 