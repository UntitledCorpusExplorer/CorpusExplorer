import { useCallback, memo } from 'react';
import { Handle, Position, useStore } from 'reactflow';
import WindowFactory from '../WindowFolder/WindowFactory';
import { NodeResizer } from '@reactflow/node-resizer';
import '@reactflow/node-resizer/dist/style.css';

function WindowNode({ data, id, selected }) {

  const size = useStore((s) => {
    const node = s.nodeInternals.get(id);
  
    return {
      width: node.width,
      height: node.height,
    };
  });

  if (data.type == "FABMenu") {
    return (
      <>
        <NodeResizer color="#ff0071" isVisible={selected} minWidth={100} minHeight={30}   />
        <WindowFactory id={data.i} windata={data} /> 
      </>
    );
  }




  return (
    <>
        
      <NodeResizer color="#ff0071" isVisible={selected} minWidth={100} minHeight={30}   />
      <Handle type="target" position={Position.Left} />
      <WindowFactory id={data.i} size={size} windata={data} /> 
      <Handle type="source" position={Position.Right} id="a" />
  
    </>
  );
}


export default memo(WindowNode);
